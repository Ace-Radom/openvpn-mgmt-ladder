import json
import os

from app import config


def token_exists(token: str) -> bool:
    index_path = os.path.join(config.config["link"]["store_dir"], "index.json")
    if not os.path.exists(index_path):
        return False
    
    with open(index_path, "r", encoding="utf-8") as rf:
        index = json.load(rf)

    tokens = index.get("tokens", [])
    exists = token in (tokens if isinstance(tokens, list) else tokens.values())

    return exists

def get_links(token: str) -> list[str] | None:
    links_path = os.path.join(config.config["link"]["store_dir"], f"{token}.json")
    if not os.path.exists(links_path):
        return None
    
    with open(links_path, "r", encoding="utf-8") as rf:
        links = json.load(rf)

    if not isinstance(links, list):
        return None
    
    return links
