from telethon import TelegramClient, events, sync
import os

def should_fwd_event(event, src_channel):
    if event.photo:
        return True
    if event.message.message:
        text = event.message.message.lower()
        keyphrases = ["mumbai", "available"]
        for k in keyphrases:
            if k in text:
                return True
    return False

def register_event_handlers(client, slot_channels):
    for src_channel in slot_channels:
        #This function listens for new messages in the dropbox channel. You can change it to the VAC channel if you want
        @client.on(events.NewMessage(chats=src_channel))    #select channel you want to monitor
        async def my_event_handler(event):
            if should_fwd_event(event, src_channel):
                #notify("image -", event.raw_text)
                print (type(event.message.message))
                print (event.message.message)
                await client.send_message(entity=entity,message=event.message)

if __name__ == "__main__":
    #get this by creating a new bot. Message BotFather with /newbot request
    api_id = 22560527
    api_hash = 'cf3530dae96b1931d98691e59b385221'
    client = TelegramClient('anon', api_id, api_hash)
    
    #This function creates a notification on MacOS when the python script is running
    def notify(title, text):
        os.system("""
                  osascript -e 'display notification "{}" with title "{}"'
                  """.format(text, title))
    
    SLOT_CHANNELS = [       # Set of channels to monitor for slot avaiability
      "USB1B2VisaSlots",
      "B1B2SlotAvailability",
      "bcategoryslot",
      "hgcheeku_src"                    # test channel
    ] 
    
    register_event_handlers(client, SLOT_CHANNELS)

    client.start()
    entity=client.get_entity('hgcheeku')#channel you want to forward the filtered messages to 
    client.run_until_disconnected()
