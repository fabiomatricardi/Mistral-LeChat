from mistralai import Mistral
import sys
import warnings
warnings.filterwarnings(action='ignore')
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("\033[94;1m")  #light blue bold
APIK = input('Your Mistral API key: ') # 32 char from https://console.mistral.ai/api-keys/
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
    model = 'mistral-small-latest'
    history.append({"role": "user","content": prompt})
    response = CLIENT.chat.complete(model=model,
        messages = history)
    answer = response.choices[0].message.content
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
    print(new_message)
