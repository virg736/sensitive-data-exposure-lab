"""
check_passwords.py

Script éducatif de vérification de mots de passe.
Usage pédagogique uniquement.
"""

WEAK_PASSWORDS = [
    "password",
    "123456",
    "admin",
    "admin123",
    "qwerty"
]

TEST_PASSWORDS = [
    "SecurePass!2025",
    "MyStrongPwd#42"
]

def is_weak(password):
    return password.lower() in WEAK_PASSWORDS

def main():
    print("=== Password Security Check (CI mode) ===")

    weak_found = False

    for pwd in TEST_PASSWORDS:
        if is_weak(pwd):
            print(f"[WEAK] Password detected: {pwd}")
            weak_found = True
        else:
            print(f"[OK] Password is strong: {pwd}")

    if weak_found:
        print("⚠️ Weak passwords detected (informational).")
    else:
        print("✅ No weak passwords detected.")

if __name__ == "__main__":
    main()