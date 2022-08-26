from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.asgi import GraphQL
from ariadne.constants import PLAYGROUND_HTML
from query_resolvers import listPosts_resolver, getPost_resolver, listComments_resolver, getComment_resolver
from mutation_resolver import create_post_resolver, update_post_resolver, delete_post_resolver, create_comment_resolver, update_comment_resolver, delete_comment_resolver

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)
query.set_field("listComments", listComments_resolver)
query.set_field("getComment", getComment_resolver)


mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)
mutation.set_field("createComment", create_comment_resolver)
mutation.set_field("updateComment", update_comment_resolver)
mutation.set_field("deleteComment", delete_comment_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

app = GraphQL(schema, debug=True)
