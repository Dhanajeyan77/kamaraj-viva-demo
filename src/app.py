import hashlib

# ❌ VULNERABILITY: Hardcoded Credential
DATABASE_KEY = "Kamaraj_Admin_2026_Secure!"

def insecure_login(user_pass):
    # ❌ VULNERABILITY: Using MD5 (Weak/Broken Hashing)
    hashed = hashlib.md5(user_pass.encode()).hexdigest()
    print(f"Logging in with hash: {hashed}")