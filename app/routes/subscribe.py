import base64

from app import links
from flask import Blueprint, jsonify, make_response

bp = Blueprint("subscribe", __name__)


@bp.route("/subscribe/<token>")
def subscribe(token: str):
    if not links.token_exists(token):
        return jsonify(
            {
                "success": False,
                "msg": "Token doesn't exist",
            },
            404
        )
    
    link_list = links.get_links(token)
    if link_list is None:
        return jsonify(
            {
                "success": False,
                "msg": "Link list with this token doesn't exist",
            },
            500
        )
    
    link_str = ""
    for link in link_list:
        link_str += link
        link_str += "\n"

    links_b64 = base64.urlsafe_b64encode(link_str.encode("utf-8")).decode("utf-8")
    response = make_response(links_b64)
    response.mimetype = "text/plain"

    return response, 200
