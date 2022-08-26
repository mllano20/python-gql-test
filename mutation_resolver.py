from datetime import date

from ariadne import convert_kwargs_to_snake_case

from db import db
from models import Post


@convert_kwargs_to_snake_case
def create_post_resolver(_, info, input):
    try:
        post = {"title": input["title"], "body": input["body"],
                "userId": input["user_id"], "id": input["id"]}
        db.create_post(post)
        payload = {
            "success": True,
            "post": post
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Error creating post"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_post_resolver(_, info, id, input):
    try:
        post = {"title": input["title"], "body": input["body"],
                "userId": input["user_id"], "id": input["id"]}
        db.update_post(id, post)
        payload = {
            "success": True,
            "post": post
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver(_, info, id):
    try:
        if db.delete_post(id):
            payload = {"success": True}
        else:
            payload = {"success": False,   "errors": ["Not found"]}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def create_comment_resolver(_, info, input):
    try:
        comment = {"name": input["name"], "body": input["body"],
                   "postId": input["post_id"], "id": input["id"], "email": input["email"]}
        db.create_comment(comment)
        payload = {
            "success": True,
            "comment": comment
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Error creating comment"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_comment_resolver(_, info, id, input):
    try:
        comment = {"name": input["name"], "body": input["body"],
                   "postId": input["post_id"], "id": input["id"], "email": input["email"]}
        db.update_comment(id, comment)
        payload = {
            "success": True,
            "comment": comment
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def delete_comment_resolver(_, info, id):
    try:
        if db.delete_comment(id):
            payload = {"success": True}
        else:
            payload = {"success": False,   "errors": ["Not found"]}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
