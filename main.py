from mccurdy import mccurdyChat
from austin import austinChat
from brendan import brendanChat


def chat(text):

  response = mccurdyChat(text)

  if response:
    return response

  response = austinChat(text)

  if response:
    return response

  response = brendanChat(text)
  
  if response:
    return response
    
  return "I'm still learning.  Try saying hello."

while(True):
  userInput = input(">>> ")
  print(chat(userInput))