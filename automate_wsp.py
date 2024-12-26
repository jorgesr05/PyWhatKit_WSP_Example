import pywhatkit as kit
import datetime

now = datetime.datetime.now()

hour = now.hour
minute = now.minute + 1

if minute == 60:
    minute = 0
    hour += 1


kit.sendwhatmsg(
    "Put the number to which the message will be sent e.g. +51 999-999-xxx (Peru)",
    "Put your message",
    hour,
    minute
)


