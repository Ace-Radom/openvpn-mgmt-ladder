import base64

from app import data
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
    
    server_str = ""
    for link in server_list:
        server_str += link
        server_str += "\n"

    links_b64 = base64.urlsafe_b64encode(server_str.encode("utf-8")).decode("utf-8")
    response = make_response(links_b64)
    response.mimetype = "text/plain"

    return response, 200
