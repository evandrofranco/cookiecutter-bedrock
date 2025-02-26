import pytest
import sys


sys.path.insert(0, ".")
sys.path.insert(1, "..")


from bedrock import Bedrock


def test_invoke_01():
    model = "amazon.nova-micro-v1:0"
    msg = "Hello. What can you do?"

    bedrock = Bedrock(model)

    elapsed, predicted, token_usage = bedrock.invoke(input_msg=msg)

    print(f'Elapsed {elapsed}')
    print(predicted)
    print(token_usage)
    
    assert elapsed < 5 #5s latency
    assert token_usage["outputTokens"] >= 100 #msg size


def test_invoke_with_image_01():
    
    model = "amazon.nova-pro-v1:0"
    msg = """What the following code are doing? Please explain using tags <thinking></thinking> 
              and give a final answer on tags <answer></answer>"""
    img = "img/code-block-1.png"
    img_mime_type = 'png'

    bedrock = Bedrock(model)

    elapsed, predicted, token_usage = bedrock.invoke(input_msg=msg, input_image=img, image_mime_type=img_mime_type)

    print(f'Elapsed {elapsed}')
    print(predicted)
    print(token_usage)


def test_invoke_with_image_02():
    
    model = "amazon.nova-lite-v1:0"
    msg = """What the following code are doing? Please explain using tags <thinking></thinking> 
              and give a final answer on tags <answer></answer>"""
    img = "img/code-block-1.png"

    bedrock = Bedrock(model)

    try:
        bedrock.invoke(input_msg=msg, input_image=img)
        assert False
    except:
        assert True