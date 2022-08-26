# Python-GQL-Test
A Python GraphQL Server with Ariadne

## Integration

Class to integrate with a Public API (https://jsonplaceholder.typicode.com/). Syncs the data in the public API with a local PostgreSQL database.

### Available methods:

```GET 	/posts
GET 	/posts/1
GET 	/posts/1/comments
GET 	/comments?postId=1
POST 	/posts
PUT 	/posts/1
PATCH 	/posts/1
DELETE 	/posts/1
```
## GraphQL Server

Provides endpoints to read and write data to the DB. 

### Available methods:

- Queries: 
    - listPosts
    - getPost
    - listComments
    - getComment

- Mutations:
    - createPost
    - updatePost
    - deletePost
    - createComment
    - updateComment
    - deleteComment

## How to Run

Build Docker image:

```
sudo docker build -t python-gqlserver .
```

Run Docker container on Linux:

```
sudo docker run  -p 8000:8000 --net=host --env-file .env python-gqlserver:latest
```