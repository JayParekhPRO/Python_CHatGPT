#Author : Jay Parekh

#Importing the modules
import openai

#Setting the API key
openai.api_key="API_key"

#Setting the Botname
Bot_Name = "BotName"

#Introduction
print(" \n\n\n Hi , I am "+Bot_Name+" \n I will help you with all your Questions ")

#Chatbot
while 1==1 :
    Question = input("\n User : ")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": Question}])
    print(Bot_Name+" : "+completion.choices[0].message.content)