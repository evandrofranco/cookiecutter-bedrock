from bedrock import Bedrock

if __name__ == '__main__':
    
    model = "amazon.nova-pro-v1:0" # Change you model here
    msg = "Please describe following card" # Change your message here
    img = "img/murkrow2.jpeg"

    bedrock = Bedrock(model)

    elapsed, predicted, token_usage = bedrock.invoke_with_image(img, msg)

    print(f'Elapsed {elapsed}')
    print(predicted)
    print(token_usage)