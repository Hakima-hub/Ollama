import ollama_101_utils as utils
from ollama import chat

print("To exit please type 'exit'")
user_input = utils.getUserQuery(messages=utils.messages, machine_question_nudge= 'Give me something to summarize...')

while True:
    if(user_input == 'exit'):
        print('sropping...')
        break
    else:
        print('running...')
        user_prompt = f'<YOU>: {user_input}'
        print(user_prompt)
        print("summarizing...")
        response = utils.generateTextSummary(Model=utils.MODEL, text = user_input)
        print('\n<MACHINE THinker summary>: ')
        print(response)

    user_input = utils.getUserQuery(messages=utils.messages, machine_question_nudge= "Give me more to summarize...")