from models import Post
from ariadne import convert_kwargs_to_snake_case

from db import db


def listPosts_resolver(obj, info):
    try:
        posts = db.read_post()
        payload = {
            "success": True,
            "post": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = db.read_post(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"item matching id {id} not found"]
        }

    return payload


def listComments_resolver(obj, info):
    try:
        comments = db.read_comment()
        payload = {
            "success": True,
            "comments": comments
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getComment_resolver(obj, info, id):
    try:
        comment = db.read_comment(id)
        payload = {
            "success": True,
            "comment": comment
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"item matching id {id} not found"]
        }

    return payload
