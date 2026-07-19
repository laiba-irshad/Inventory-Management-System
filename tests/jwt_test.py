from app.utils.jwt import create_access_token, verify_access_token

token = create_access_token(
    {
        "user_id": 1,
        "username": "admin",
        "role": "ADMIN"
    }
)

print("Token:")
print(token)

print()

payload = verify_access_token(token)

print("Decoded Payload:")
print(payload)