import ollama_101_utils as utils
from ollama import generate

user_input = utils.getuserquery(messages = utils.messages)
while True:
    if (user_input == 'text'):
        print('stopping...')
        break
    else:
        print('running...')
        user_prompt = f'<YOU>:{ user_input}'
        print(user_prompt)
        response = utils.getUsersummary( messages = utils.messages, model= utils.MODEL)
        machine_response = ('\n<MACHINE Thinker>':)
    for chunk in response:
        print(chunk.message.response, end='', flush=True)

user_input = utils.getuserQuery(messages=utils.messages)