from py_imessage import imessage 
from time import sleep 

phone = input("Enter a phone number: ")

if not imessage.check_compatibility(phone):
	print("not an iPhone")

guid = imessage.send(phone, "sorry testing something one last one")

sleep(5)
resp = imessage.status(guid)

print(f'Message read at {resp.get("date_read")}')