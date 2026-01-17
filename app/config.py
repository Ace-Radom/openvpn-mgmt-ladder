import configparser

config = {
    "app": {"is_production_env": False},
    "link": {
        "store_dir": "/var/openvpn-mgmt/ladder/link"
    }
}


def parse_config(config_path: str) -> None:
    parser = configparser.ConfigParser()
    parser.read(config_path)

    if (parser.has_section("app")):
        if parser.has_option("app", "is_production_env") and len(parser["app"]["is_production_env"]) != 0 and parser["app"]["is_production_env"].isdigit():
            config["app"]["is_production_env"] = int(parser["app"]["is_production_env"]) != 0
        
    if parser.has_section("link"):
        if parser.has_option("link", "store_dir") and len(parser["link"]["store_dir"]) != 0:
            config["link"]["store_dir"] =  parser["link"]["store_dir"]

    return
