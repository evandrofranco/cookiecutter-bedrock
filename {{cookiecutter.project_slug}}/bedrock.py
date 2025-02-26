"""Module for interacting with Amazon Bedrock Runtime.

This module provides an interface for invoking Amazon Bedrock models
"""

import boto3
import time
import logging

class Bedrock:
    """Class to manage interactions with Amazon Bedrock Runtime.

    This class provides methods to invoke Bedrock models with support
    for text and image inputs.

    Attributes:
        bedrock_client: Boto3 client for bedrock-runtime service
        bedrock_model: Bedrock model ID to be used
        logger: Logger for execution information
    """

    def __init__(self, model):
        """Initialize a new Bedrock client instance.

        Args:
            model (str): Bedrock model ID to be used
        """
        self.bedrock_client = boto3.client(service_name="bedrock-runtime")
        self.bedrock_model = model
        self.logger = logging.getLogger(__name__)
        

    def invoke(self,
               input_msg,
               system_msg=None, 
               input_image=None,
               image_mime_type=None,
               inference_config_params=None,
               additional_params=None):
        """Invoke the Bedrock model with the provided inputs.

        Args:
            input_msg (str): Main text message for the model
            system_msg (str, optional): System message for context
            input_image (str, optional): Path to image file
            image_mime_type (str, optional): Image MIME type (e.g., '.png')
            inference_config_params (dict, optional): Inference configuration parameters
            additional_params (dict, optional): Additional model parameters

        Returns:
            tuple: (elapsed_time, predicted_text, token_usage)
                - elapsed_time (float): Execution time in seconds
                - predicted_text (str): Text generated by the model
                - token_usage (dict): Token usage statistics

        Raises:
            ValueError: If input_image is provided without image_mime_type
        """
        self.logger.info(f"Invoking model {self.bedrock_model} with image")
        
        # Base Prompts
        content = [{"text": input_msg}]
        system_prompts = []
        # Base inference parameters to use.
        inference_config = {}
        # Additional inference parameters to use.
        additional_model_fields = {}

        # Filling values if exists
        if inference_config:
            inference_config.update(inference_config_params)

        # Filling values if exists
        if additional_model_fields:
            additional_model_fields.update(additional_params)

        # Filling values if exists
        if input_image:
            if not image_mime_type:
                raise ValueError(
                    "Please provide image_mime_type parameter with your file extension, "
                    "example: image_mime_type='.png'"
                )
            with open(input_image, "rb") as f:
                image = f.read()

            content.append({
                "image": {
                    "format": image_mime_type,
                    "source": {
                        "bytes": image
                    }
                }
            }) 

        # Filling values if exists
        if system_msg:
            system_prompts.append({"text": system_msg})
        
        # Filling values if exists
        message = {
                    "role": "user",
                    "content": content
        }

        messages = [message]

        start_time = time.time()
        
        # Send the message.
        response = self.bedrock_client.converse(
            modelId=self.bedrock_model,
            system=system_prompts,
            messages=messages,
            inferenceConfig=inference_config,
            additionalModelRequestFields=additional_model_fields

        )
        end_time = time.time()
        elapsed = end_time - start_time

        output_message = response['output']['message']
        predicted = ""
        for content in output_message['content']:
            answer = content['text']
            predicted += answer    
        self.logger.info(f"Bedrock Prediction with model {self.bedrock_model} for image {input_image}")
        self.logger.info(f"Predicted Text: {predicted}")

        token_usage = response['usage']
        self.logger.info(f"Input tokens:  {token_usage['inputTokens']}")
        self.logger.info(f"Output tokens:  {token_usage['outputTokens']}")
        self.logger.info(f"Total tokens:  {token_usage['totalTokens']}")

        return elapsed, predicted, token_usage