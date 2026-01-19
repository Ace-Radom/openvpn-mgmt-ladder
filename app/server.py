import base64
import json
import os

from app import config

def generate_msg_server_link(msg: str) -> str:
    data = {
        "v": 2,
        "ps": msg,
        "add": "127.0.0.1",
        "port": "54321",
        "id": "45d5e4cc-46af-4ced-a1ad-2614b0d0fc19", # just some random stuff
        "aid": "0",
        "net": "tcp",
        "type": "none",
        "host": "",
        "tls": ""
    }
    data_str = base64.urlsafe_b64encode(json.dumps(data).encode("utf-8")).decode("utf-8")
    return f"vmess://{data_str}"

def generate_server_msg_server_link_list() -> list[str] | None:
    server_msg_path = os.path.join(config.config["data"]["store_dir"], f"server_msg.json")
    if not os.path.exists(server_msg_path) or not os.path.isfile(server_msg_path):
        return None
    
    with open(server_msg_path, "r", encoding="utf-8") as rf:
        server_msgs = json.load(rf)

    if not isinstance(server_msgs, list):
        return None
    
    server_msg_server_link_list = []
    for msg in server_msgs:
        server_msg_server_link_list.append(generate_msg_server_link(msg))

    return server_msg_server_link_list
