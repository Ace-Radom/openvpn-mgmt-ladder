import json
import os

from app import config


def read_index() -> dict | None:
    index_path = os.path.join(config.config["data"]["store_dir"], "index.json")
    if not os.path.exists(index_path) or not os.path.isfile(index_path):
        return None
    
    with open(index_path, "r", encoding="utf-8") as rf:
        index = json.load(rf)

    return index

def token_exists(token: str) -> bool:
    index = read_index()
    if index is None:
        return False
    if not isinstance(index["tokens"], list):
        return False
    
    return token in index["tokens"]

def get_server_list(token: str) -> list[str] | None:
    server_list_path = os.path.join(config.config["data"]["store_dir"], f"{token}.json")
    if not os.path.exists(server_list_path) or not os.path.isfile(server_list_path):
        return None
    
    with open(server_list_path, "r", encoding="utf-8") as rf:
        server_list = json.load(rf)

    if not isinstance(server_list, list):
        return None
    
    return server_list
