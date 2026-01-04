"""
check_passwords.py
Script éducatif de vérification de mots de passe faibles.

Objectif :
- Détecter des mots de passe trop simples
- Sensibiliser aux bonnes pratiques de sécurité
- Usage pédagogique uniquement
"""

# Liste de mots de passe faibles courants (exemples)
WEAK_PASSWORDS = [
    "password",
    "123456",
    "123456789",
    "admin",
    "admin123",
    "qwerty",
    "letmein",
    "welcome",
    "password123"
]


def check_password(password: str) -> bool:
    """
    Vérifie si le mot de passe est faible.
    Retourne True si le mot de passe est faible, False sinon.
    """
    if len(password) < 8:
        return True

    if password.lower() in WEAK_PASSWORDS:
        return True

    return False


def main():
    print("=== Password Security Check ===")
    user_password = input("Enter a password to check: ")

    if check_password(user_password):
        print("[WARNING] Weak password detected!")
        print("Please choose a stronger password.")
    else:
        print("[OK] Password looks strong.")


if __name__ == "__main__":
    main()
