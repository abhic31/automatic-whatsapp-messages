# automatic-whatsapp-messages
this will send automated messaged to users
if you want to send to a group add 
import time
import pywhatkit as kit
import datetime

# Parameters
group_id = "your_group_id_here"  # Replace "your_group_id_here" with the group ID
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
#how to get group _id
Extract Group ID from Link: The link will look like https://chat.whatsapp.com/XXXXXXXXXXXXXXX, where XXXXXXXXXXXXXXX is the group ID.
