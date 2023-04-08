import random
import string


def generate_password(security_level, password_length) -> str:
    letters_upper = [x for x in string.ascii_uppercase]
    letters_lower = [x for x in string.ascii_lowercase]
    numbers = [str(x) for x in range(10)]
    special_chars = [x for x in string.punctuation]

    easy_chars = letters_upper + letters_lower

    medium_chars = letters_upper + letters_lower + numbers

    strong_chars = letters_upper + letters_lower + numbers + special_chars

    def easyFun() -> str:
        has_letter_up = False
        has_letter_low = False
        password = ''
        check = False
        while not check or len(password) < password_length:
            if len(password) >= password_length:
                password = ''
                has_letter_up = False
                has_letter_low = False
            new_char = random.choice(easy_chars)
            password += new_char
            if new_char in letters_upper:
                has_letter_up = True
            if new_char in letters_lower:
                has_letter_low = True
            check = has_letter_low and has_letter_up
        return password

    def mediumFun() -> str:
        password = ''
        has_num = False
        has_letter_up = False
        has_letter_low = False
        check = False
        while not check or len(password) < password_length:
            if len(password) >= password_length:
                password = ''
                has_num = False
                has_letter_up = False
                has_letter_low = False
            new_char = random.choice(medium_chars)
            password += new_char
            if new_char in letters_upper:
                has_letter_up = True
            if new_char in letters_lower:
                has_letter_low = True
            if new_char in numbers:
                has_num = True
            check = has_num and has_letter_up and has_letter_low
        return password

    def strongFun() -> str:
        password = ''
        has_num = False
        has_punctuation = False
        has_letter_up = False
        has_letter_low = False
        check = False
        while not check or len(password) < password_length:
            if len(password) >= password_length:
                password = ''
                has_num = False
                has_punctuation = False
                has_letter_up = False
                has_letter_low = False
            new_char = random.choice(strong_chars)
            password += new_char
            if new_char in numbers:
                has_num = True
            if new_char in special_chars:
                has_punctuation = True
            if new_char in letters_upper:
                has_letter_up = True
            if new_char in letters_lower:
                has_letter_low = True
            check = has_num and has_punctuation and has_letter_up and has_letter_low
        return password

    if security_level == "Easy":
        return easyFun()
    if security_level == "Medium":
        return mediumFun()
    if security_level == "Strong":
        return strongFun()
