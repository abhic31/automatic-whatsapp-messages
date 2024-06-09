import time
import pywhatkit as kit
import datetime

# Parameters
phone_number = "+91**********"  
messages = [
    "hi what are you doing?",
    "you know much how much",
    "its a big day",
    "yesterday was a first rain",
    "How's your day going?",
    "Have you eaten yet?",
    "Thinking of you!",
    "Did you hear about the latest news?",
    "Hope you're having a great day!",
    "Just wanted to say hello!",
    "Remember to take care of yourself!",
    "Wishing you all the best!",
]

# Current time
now = datetime.datetime.now()
current_hour = now.hour
current_minute = now.minute + 1  

for message in messages:
    kit.sendwhatmsg_instantly(phone_number, message, current_hour, current_minute)
    time.sleep(5)  # Adjust this value if needed to avoid rate limiting or message sending issues
