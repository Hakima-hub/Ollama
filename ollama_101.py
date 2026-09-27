import ollama_101_utils as utils

# prompting section 
print("To exit please type 'exit'")
user_input = utils.getUserQuery(messages=utils.messages) 

while True:  
    if (user_input == "exit"):
        print("stopping...")
        break
    else: 
        print("running...")
        user_prompt = f"<YOU>: {user_input}"
        print(user_prompt)
        response = utils.streamChatReponse(messages=utils.messages, model=utils.MODEL)
        machine_response = ("\n<MACHINE Thinker>: ")
        for chunk in response:
            print(chunk.message.content, end='', flush=True)

user_input = utils.getUserQuery(messages=utils.messages)