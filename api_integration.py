from email.mime import base
import requests
from jsonschema import validate

from schemas import post_schema, put_schema
from db import db

base_url = "https://jsonplaceholder.typicode.com"


class Integration():

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_posts(self, post_id: int = None) -> bool:
        if post_id:
            try:
                response = requests.get(self.base_url+"/posts/"+str(post_id))
                if response.status_code == 200:
                    db.create_post(response.json())
                    return True
                else:
                    return False
            except:
                return False
        else:
            try:
                response = requests.get(self.base_url+"/posts")
                if response.status_code == 200:
                    for r in response.json():
                        db.create_post(r)
                    return True
                else:
                    return False
            except:
                return False

    def get_comments(self, post_id: int = None) -> bool:
        if post_id:
            try:
                response = requests.get(
                    self.base_url+"/posts/"+str(post_id)+"/comments")
                if response.status_code == 200:
                    for r in response.json():
                        db.create_comment(r)
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False

    def post_posts(self, body: dict) -> bool:
        try:
            validate(body, schema=post_schema)
            response = requests.post(self.base_url+"/posts", data=body)
            if response.status_code == 201:
                db.create_post(body)
                return True
            else:
                return False
        except:
            return False

    def put_posts(self, body: dict) -> bool:
        try:
            validate(body, schema=put_schema)
            response = requests.put(
                self.base_url+"/posts/"+str(body["id"]), data=body)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def patch_posts(self, body: dict) -> bool:
        try:
            validate(body, schema=put_schema)
            response = requests.patch(
                self.base_url+"/posts/"+str(body["id"]), data=body)
            if response.status_code == 200:
                db.update_post(body)
                return True
            else:
                return False
        except:
            return False

    def delete_posts(self, post_id: int = None) -> bool:
        if post_id:
            try:
                response = requests.delete(
                    self.base_url+"/posts/"+str(post_id))
                if response.status_code == 200:
                    db.update_post
                    return True
                else:
                    return False
            except:
                return False
        return False
