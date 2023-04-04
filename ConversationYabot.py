
import random

# opcoes = ['pedra', 'papel', 'tesoura']

class ConversationFlow():
   def __init__(self):
      self.state = 'menu'
      self.data = {}

   def processInput(self, inputText, hasMedia):
      if hasMedia > 0:
         return 
         return "Thanks for the image. Here's one for you!"
      
      else:
         xingamentos = [
            'Vai se ferrar Yama!', 
            'Cala boca vagabundo!', 
            'Se fuder.',
            'oi o krl, se fuder.',
            'sua vagabunda.'
         ]

         return random.choice(xingamentos)

         
#             return f'''
# *MENU:*
# - TASK 1:
# --- SUBTASK 1.1
# --- SUBTASK 1.2

# - TASK 2:
# --- SUBTASK 2.1
# --- SUBTASK 2.2

# - TASK 3:
# --- SUBTASK 3.1
# --- SUBTASK 3.2
# --- SUBTASK 3.3
# --- --- SUBSUBTASK 3.3.1
# --- --- SUBSUBTASK 3.3.2
# '''



# flow = ConversationFlow()

# while True:
#    incomingMessage = input("> ")
#    response = flow.processInput(incomingMessage)

#    print(response)