
import json
import uuid


def show_json():
   with open('messages.json', encoding='utf-8') as f:
      data = json.load(f)

   print(data)


def write_json(dia_mes, dias_num, horario, message, filename='messages.json'):
   new_data = {
      "dia_mes": None,
      "dias_num": None,
      "horario": None,
      "message": None
   }

   # dia_mes = input("Dias do Mês: ")
   # dia_mes = transforma_input(dia_mes)
   # dias_num = input("Dias da Semana: ")
   # dias_num = transforma_input(dias_num)
   # horario = input("Horário da Mensagem: ")
   # message = input("Mensagem: ")

   lista = [dia_mes, dias_num, horario, message]

   for i, (k, v) in enumerate(new_data.items()):
      new_data[k] = lista[i]

   with open(filename,'r+') as file:
      file_data = json.load(file)

      # new_data["id"] = file_data["YABOT"][len(file_data["YABOT"]) - 1]["id"] + 1 if len(file_data["YABOT"]) >= 1 else 1
      new_data["id"] = str(uuid.uuid4())
      file_data["YABOT"].append(new_data)
      file.seek(0)
      json.dump(file_data, file, indent = 3)

   print("New data has been added. | write_json()")


def remove_json(id_, filename='messages.json'):
   with open(filename, 'r+') as file:
      file_data = json.load(file)

   for i in file_data["YABOT"]:
      if id_ == i['id']:
         pos = file_data["YABOT"].index(i)
         file_data["YABOT"].pop(pos)
         with open(filename, 'w') as file:
            json.dump(file_data, file, indent=3)

         print(f"ID ({id_}) has been removed. | remove_json()")
         break   

   else:
      print(f"ID ({id_}) does not exist! | remove_json()")


def resumo_json(filename='messages.json'):
   with open(filename, 'r') as file:
      data = json.load(file)
   
   resumo = "Resumo das Mensages: "
   for data in data["YABOT"]:
      resumo += f"@#! ID {data['id']}) {data['message']} ({data['horario']})"

   resumo = resumo.replace('@#! ', '\n')

   print(f"{resumo} | resumo_json()")


def transforma_input(input_):
   data = input_.split()
   input_transformado = list(map(int, data))

   if len(input_transformado) == 0:
      return None
   else:
      return input_transformado


def sendMessage(message):
   print(message)


estado = 0
while True:
   wpp = input("> ")

   if wpp == 'ADD':
      estado = 'add0'

      while estado != 0:               
         if estado == 'add0':
            dias = input("Entre os dias da mensagem ou o mês. ")
            dias = dias.lower()

            if "dia" in dias:
               dias = dias.replace("dias ", "").strip()

               dia_mes = transforma_input("")
               dias_num = transforma_input(dias)

            if "mes" in dias or "mês" in dias:
               dias = dias.replace("mes ", "").strip()

               dia_mes = transforma_input(dias)
               dias_num = transforma_input("")

            estado = 'add1'

         if estado == 'add1':
            horario = input("Entre o horário de envio da mensagem [XX:XX]. ")

            estado = 'add2'

         if estado == 'add2':
            message = input("Entre a mensagem para ser enviada. ")

            estado = 'add3'

         if estado == 'add3':
            write_json(dia_mes, dias_num, horario, message)
            print("EVENTO ADICIONADO")

            estado = 0
