import boto3
import time
import logging

class Bedrock():

    def __init__(self, model):
        self.bedrock_client = boto3.client(service_name="bedrock-runtime")
        self.bedrock_model = model
        self.logger = logging.getLogger(__name__)
        

    def invoke_with_image(self,
                          input_image,
                          input_msg):

        self.logger.info(f"Invoking model {self.bedrock_model} with image")
        
        with open(input_image, "rb") as f:
            image = f.read()

        message = {
            "role": "user",
            "content": [
                {
                    "text": input_msg
                },
                {
                        "image": {
                            "format": 'jpeg',
                            "source": {
                                "bytes": image
                            }
                        }
                }
            ]
        }
        messages = [message]

        start_time = time.time()
        # Send the message.
        response = self.bedrock_client.converse(
            modelId=self.bedrock_model,
            messages=messages
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