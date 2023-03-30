
import random

opcoes = ['pedra', 'papel', 'tesoura']

class ConversationFlow():
   def __init__(self):
      self.state = 'start'
      self.data = {}

   def processInput(self, inputText):
      if self.state == 'start':
         self.data = {}
         self.state = 'play?'
         return "Olá, gostaria de Jogar Jokenpô?"
      
      elif self.state == 'play?':
         if inputText in ['sim', 's']:
            self.state = 'jokenpo'
            return "Mande sua escolha!"

         elif inputText in ['não', 'nao', 'n']:
            self.state = 'start'
            return 'Ok até mais tarde!'

         else:
            self.state = 'play?'
            return 'Não entendi, repete por favor?'
         
      elif self.state == 'jokenpo':
         pc = random.choice(opcoes)
         self.data['pc'] = pc

         self.data['me'] = inputText

         escolhas = f'PC: {self.data["pc"]}\nVocê: {self.data["me"]}'
         if self.data['pc'] == self.data['me']:
            return f'{escolhas}\nEmpatou'
         
         elif self.data['pc'] == 'pedra':
            if self.data['me'] == 'papel':
               return f'{escolhas}\nVocê Ganhou!'
            
            elif self.data['me'] == 'tesoura':
               return f'{escolhas}\nVocê Perdeu!'
            
         elif self.data['pc'] == 'tesoura':            
            if self.data['me'] == 'pedra':
               return f'{escolhas}\nVocê Ganhou!'
            
            elif self.data['me'] == 'papel':
               return f'{escolhas}\nVocê Perdeu!'
            
         elif self.data['pc'] == 'papel':
            if self.data['me'] == 'tesoura':
               return f'{escolhas}\nVocê Ganhou!'

            elif self.data['me'] == 'pedra':
               return f'{escolhas}\nVocê Perdeu!'
         
         self.state = 'start'
         



# flow = ConversationFlow()

# while True:
#    incomingMessage = input("> ")
#    response = flow.processInput(incomingMessage)

#    print(response)