import re

def evaluate_password_strength(password: str) -> tuple[str, str]:
    score = 0
    length = len(password)

    if length >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/~`]", password):
        score += 1

    if length < 6:
        return "Very Weak", "red"
    elif score <= 2:
        return "Weak", "orange"
    elif score == 3 or score == 4:
        return "Medium", "blue"
    else:
        return "Strong", "green"
