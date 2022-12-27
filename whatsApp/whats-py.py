import pywhatkit

pywhatkit.sendwhatmsg("Phone Number", "Message", 13, 59, 15, True, 5)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("Group Id", "Images-path", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("Phone Number", "Images-path")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("Group Id", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("Group Id", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit")