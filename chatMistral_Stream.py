from mistralai import Mistral
import sys
import warnings
warnings.filterwarnings(action='ignore')
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("\033[94;1m")  #light blue bold
APIK = input('Your Mistral API key: ') #'jspAEJOmr87tF7R7yMmgYyEgKbQDKR0c'
CLIENT = Mistral(api_key=APIK)
history = []

print("\033[93;1m")  #light yellow
intro = """
                                                                           
 ░░░               ░░                                                      
 ▒█▒░░░░          ░█▓░░░░                                                  
 ▒█▒░░░░          ░█▓░░░░                                                  
 ▒█▒░░░░░░░░  ▒█▒░░░░░░░░       ▓▓    ▓▓▒▒▒      ░▓▓▓▓░▓▒  █▒  ▓█▓ ░▓▓█▓▒  
 ▒█▒░░░░░░░░  ▒█▒░░░░░░░░       ▓▓    ▓▓▒▒░      █▒    ▓▓▒▒█▒ ░█▒█░  ▒▓    
 ▒█▒▒▒▒▒▒▒░░░░▒▓▒▒▒▒▒▒▒░░       ▓▓    ▓▒         ▓▒  ▒ ▓▓ ░█▒ ▓█▓█▒  ▒▓    
 ▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ▒▓▓▓▓ ▓▓▓▓▓       ▓▓▓▒ ▓▒  ▓▒░▓  ░▓░ ▒▓    
 ▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                                                  
 ▒█▓▒▒▒░  ▓█▒▒▒▒░ ░█▓▒▒▒▒                                                  
 ▒█▓▒▒▒░  ▓█▒▒▒▒░ ░█▓▒▒▒▒       ▓█░▓█ ░▓██▓  ▓▓▓▓ ▒▓▓█▓▓░█▓▓▓▒  ▓▓▒  ░█░   
 ▒█▓▒▒▒░  ░▒░░░░  ░▓▓▒▒▒▒       ▓▒▓▓▓   ▓▓  ░█▓▒    ▒█   █▒ ▓▓ ░█░▓░ ░█░   
 ▒█▓▒▒▒▒  ▒▓  ░▓░ ░█▓▒▒▒▒       ▓▒▓░▓   ▓▓     ░▓▒  ▒█   █▒▒▓  ▓█▓█▓ ░█░   
 ▒█▓▒▒▒▒  ▓█  ▒█▒ ░▓▓▒▒▒▒       ▒▒  ▓ ░▓▓▓▓ ░▓▓▓▒   ▒▓   ▓░ ▒▓░▓░ ░▓░░▓▓▓▓░
                                                                                                          
"""
print(intro)

def chatMistral(CLIENT,history,prompt):
    """
    SDK call to Mistral Platforme endpoints for free and paid models 
    The function will STREAM the output token by token
    - it is required a verified API key from https://console.mistral.ai/
    inputs: CLIENT -> instance of Mistral object
           history -> list, chat messages
           prompt  -> str, the prompt from the user
    outputs : history -> list, chat messages including the prompt and model response
              answer  -> str, the model response to the prompt     
    Usage example:
    from mistralai import Mistral
    CLIENT = Mistral(api_key=APIK)
    history = []
    history, new_message = chatMistral(CLIENT,history,'what is Science?')
    ---
    more examples from https://docs.mistral.ai/capabilities/completion/
    """
    model = 'mistral-small-latest'
    history.append({"role": "user","content": prompt})
    temp = 0.1
    pp = 1.2
    maxtokens = 1000
    res = CLIENT.chat.stream(model=model,
        messages = history, temperature=temp, presence_penalty=pp, max_tokens=maxtokens) #presence_penalty=pp,
    answer = ''#response.choices[0].message.content
    for chunk in res:
        if chunk.data.choices[0].delta.content is not None:
            print(chunk.data.choices[0].delta.content, end="")  
            answer = answer + chunk.data.choices[0].delta.content 
    history.append({"role": "assistant", "content": answer})
    return history,answer

while True:
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break
    #history.append({"role": "user", "content": userinput})
    print("\033[92;1m")
    history, new_message = chatMistral(CLIENT,history,userinput)
    #print(new_message)