from sqlalchemy.orm import sessionmaker, scoped_session

from models import Post, Comment, session


class DB_Instance():

    def __init__(self):
        pass

    def create_post(self, body: dict) -> bool:
        try:
            post_aux = Post(title=body["title"],
                            body=body["body"], userId=body["userId"])
            session.add(post_aux)
            session.commit()
            return True
        except:
            return False

    def read_post(self, postId: int = None) -> list:
        if postId:
            try:
                posts = Post.query.get(postId)
                return posts.to_dict()
            except:
                return False
        else:
            try:
                posts = [post.to_dict() for post in Post.query.all()]
                return posts
            except:
                return False

    def delete_post(self, postId: int = None) -> bool:
        if postId:
            try:
                session.query(Post).filter_by(id=postId).delete()
                session.commit()
                return True
            except:
                return False
        return False

    def update_post(self, postId: int = None, body: dict = None) -> bool:
        if postId:
            try:
                session.query(Post).filter_by(id=postId).update(body)
                session.commit()
                return True
            except:
                return False
        return False

    def create_comment(self, body: dict):
        try:
            comment_aux = Comment(email=body["email"], body=body["body"],
                                  postId=body["postId"], id=body["id"], name=body["name"])
            session.add(comment_aux)
            session.commit()
            return True
        except:
            return False

    def read_comment(self, commentId: int = None) -> list:
        if commentId:
            try:
                comments = Comment.query.get(commentId)
                return comments.to_dict()
            except:
                return False
        else:
            try:
                comments = [comment.to_dict()
                            for comment in Comment.query.all()]
                return comments
            except:
                return False

    def delete_comment(self, commentId: int = None) -> bool:
        if commentId:
            try:
                session.query(Comment).filter_by(id=commentId).delete()
                session.commit()
                return True
            except:
                return False
        return False

    def update_comment(self, commentId: int = None, body: dict = None) -> bool:
        if commentId:
            try:
                session.query(Comment).filter_by(
                    id=commentId).update(body)
                session.commit()
                return True
            except:
                return False
        return False


db = DB_Instance()
