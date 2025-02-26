from bedrock import Bedrock

if __name__ == '__main__':
    
    model = "amazon.nova-pro-v1:0" # Change you model here
    msg = """What the following code are doing? Please explain using tags <thinking></thinking> 
              and give a final answer on tags <answer></answer>"""
    img = "img/code-block-1.png" # optional parameter to add an image or document
    img_mime_type = 'png' # if sent an image, add extension

    bedrock = Bedrock(model)

    elapsed, predicted, token_usage = bedrock.invoke(input_msg=msg, 
                                                     input_image=img, 
                                                     image_mime_type=img_mime_type)

    print(f'Elapsed {elapsed}')
    print(predicted)
    print(token_usage)