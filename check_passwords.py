"""
check_passwords.py
Script éducatif de détection de mots de passe faibles.
Compatible GitHub Actions (sans input).
"""

WEAK_PASSWORDS = [
    "password",
    "123456",
    "123456789",
    "admin",
    "admin123",
    "qwerty"
]

TEST_PASSWORDS = [
    "password",
    "SecurePass!2025",
    "admin123",
    "MyStrongPwd#42"
]

def check_password(password):
    return password in WEAK_PASSWORDS

def main():
    print("=== Password Security Check (CI mode) ===")

    weak_found = False

    for pwd in TEST_PASSWORDS:
        if check_password(pwd):
            print(f"[WEAK] Password detected: {pwd}")
            weak_found = True
        else:
            print(f"[OK] Password is strong: {pwd}")

    if weak_found:
        print("\n❌ Weak passwords detected.")
        exit(1)
    else:
        print("\n✅ No weak passwords detected.")
        exit(0)

if __name__ == "__main__":
    main()