import logging
import os

from cryptography.fernet import Fernet
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

key = "ucLD_89ftavwmH5Z8MvCM9HVd0B0PNTwau40zBg_0tI="
if not key:
    raise ValueError("シークレットキーが設定されていません")
encoded_key = key.encode()
fernet = Fernet(encoded_key)

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(level=logging.DEBUG)


@app.function("sample_function")
def handle_sample_function_event(inputs: dict, logger: logging.Logger, client: WebClient,):
    user_id = inputs["user_id"]
    ip_address = inputs["ip_address"][0]["elements"][0]["elements"][0]["text"]
    encrypted_ip_address = fernet.encrypt(ip_address.encode())
    try:
        response = client.chat_postMessage(
            channel=os.environ.get("AWS_CHANNEL_ID"),
            text=f"<@{user_id}>\n{os.environ.get("AWS_MENTION_ID")} lambda invoke --function-name test-add-ip-address-to-waf --region ap-northeast-1 {encrypted_ip_address.decode()}")
        print(response)
    except Exception as e:
        logger.exception(e)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
