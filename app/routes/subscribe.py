import base64

from app import config, data, server
from flask import Blueprint, jsonify, make_response

bp = Blueprint("subscribe", __name__)


@bp.route("/subscribe/<token>")
def subscribe(token: str):
    if not data.token_exists(token):
        return jsonify(
            {
                "success": False,
                "msg": "Token doesn't exist",
            }
        ), 404
    
    server_list = data.get_server_list(token)
    if server_list is None:
        return jsonify(
            {
                "success": False,
                "msg": "Link list with this token doesn't exist",
            }
        ), 500
    server_list_len = len(server_list)
    server_list.insert(0, server.generate_msg_server_link(f"服务器数量：{server_list_len}"))
    
    if config.config["data"]["allow_server_msg"]:
        server_msgs = server.generate_server_msg_server_link_list()
        if server_msgs is not None:
            for msg in reversed(server_msgs):
                server_list.insert(1, msg)

    server_str = ""
    for link in server_list:
        server_str += link
        server_str += "\n"

    links_b64 = base64.urlsafe_b64encode(server_str.encode("utf-8")).decode("utf-8")
    response = make_response(links_b64)
    response.mimetype = "text/plain"

    return response, 200
