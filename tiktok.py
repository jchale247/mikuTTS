from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
filePath = "chatText/tts"
Client: TikTokLiveClient = TikTokLiveClient(unique_id="@jciswatchinglive")

@Client.on("connect")
async def on_connect(_: ConnectEvent):
    print(f"connected to room ID:", Client.room_id)

async def on_comment(event: CommentEvent):
    resp = event.comment
    resp = resp.lower()
    if '!miku' in resp:
        resp = resp.replace('!miku', '')
        with open(filePath + resp + ".txt", 'w') as f:
            f.write(resp)
        print(resp)

Client.add_listener("comment", on_comment)

if __name__ == '__main__':
    Client.run()
