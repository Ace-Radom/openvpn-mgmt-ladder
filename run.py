import os

from app import config, create_app

base_dir = os.path.split(os.path.realpath(__file__))[0]
config.parse_config(os.path.join(base_dir, "ladder.cfg"))

app = create_app()
if config.config["app"]["is_production_env"]:
    app.config.update(DEBUG=False)
else:
    app.config.update(DEBUG=True)

link_store_dir = config.config["link"]["store_dir"]
if not os.path.exists(link_store_dir):
    os.makedirs(link_store_dir)
if not os.path.isdir(link_store_dir):
    raise RuntimeError("Link store dir is not a directory")

if __name__ == "__main__":
    app.run()
