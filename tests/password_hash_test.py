from app.utils.hash import hash_password, verify_password

hashed = hash_password("12345678")
print(hashed)

print(verify_password("12345678", hashed))
print(verify_password("wrongpassword", hashed))