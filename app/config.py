import configparser

config = {
    "app": {"is_production_env": False},
    "data": {
        "store_dir": "/var/openvpn-mgmt/ladder/data"
    }
}


def parse_config(config_path: str) -> None:
    parser = configparser.ConfigParser()
    parser.read(config_path)

    if (parser.has_section("app")):
        if parser.has_option("app", "is_production_env") and len(parser["app"]["is_production_env"]) != 0 and parser["app"]["is_production_env"].isdigit():
            config["app"]["is_production_env"] = int(parser["app"]["is_production_env"]) != 0
        
    if parser.has_section("data"):
        if parser.has_option("data", "store_dir") and len(parser["data"]["store_dir"]) != 0:
            config["data"]["store_dir"] =  parser["data"]["store_dir"]

    return
