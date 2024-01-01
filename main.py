from graphene import ObjectType, String, Schema

class Query (ObjectType):
    hello=String(name=String(default_value="Stranger"))
    goodbye=String()

    def resolve_hello(root, info, name):
        return f"Hello {name}"

    def resolve_goodbye (root, info):
        return "Good Bye"

schema=Schema(query=Query)

query_str="{hello}" 

result=schema.execute(query_str)

print (result)
