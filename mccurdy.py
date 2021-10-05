import random
import re

def mccurdyChat(text):

  greetingOptions = ["hello", "hi", "hey", "yo", "hola", "namaste", "greetings"]

  mccurdyFavorites = {"animal":"a dog", 
                "dessert": "peanut butter balls",
                "student": "you, of course!",
                "movie": "The Matrix",}

  
  text = text.replace(",", "")
  text = text.replace(".", "")
  text = text.replace("!", "")
  text = text.replace("?","")

  textLower = text.lower()

  myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
  if myMatchObject:
    favoriteIndex = myMatchObject.group(4)
    if favoriteIndex in mccurdyFavorites:
      return "My favorite {} is {}".format(favoriteIndex, mccurdyFavorites[favoriteIndex])
  
  words = text.split(" ")
  for word in words:
    if word.lower() in greetingOptions:
      return random.choice(greetingOptions).capitalize()
    
    if word.lower() == "bye":
      return "see ya"
  
  return None
