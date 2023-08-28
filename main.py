import random
from config import *
from twilio.rest import Client

code = random.randint(100000,999999)
account_sid = sid
auth_token = token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_= gonderici,
  body= code,
  to= alici
)

ad = int(input("2 ad kodunu giriniz: "))

if ad == code:
    print("2ad kodunu doğru girdiniz")
elif ad != code:
    print("2 ad kodunu yanlış girdiniz")

