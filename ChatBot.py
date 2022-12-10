from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer  
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = Chatbot(name='PyBot', read_only = True, logic_adapters = ['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['Hola!',
              'De nada!',
              'Como estas?',
              'Que haces?',
              'Estoy bien',
              'Me siento genial',
              'Cual es tu nombre?',
              'Lo siento no te escuche',
              'Soy pybot. Hazme alguna pregunta'        
              ]


conversacion_1 = ['Mejor contenido en Instagram', 
                  ]

list_trainer = ListTrainer(my_bot)

for item in (small_talk, conversacion_1):
    list_trainer.train(item)
    
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.spanish')

print(my_bot.get_response("De nada"))
print(my_bot.get_response("El dia de hoy me siento genial!"))
print(my_bot.get_response("Cual es tu nombre?"))    

