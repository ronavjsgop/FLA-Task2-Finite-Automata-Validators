
from validators.email import validate_email

test_cases = [
    ("student@gmail.com", True),
    ("abc@yahoo.in", True),
    ("user123@outlook.com", True),
    ("john.doe@gmail.com", True),
    ("hello_123@gmail.com", True),

    ("@gmail.com", False),
    ("abc@gmail", False),
    ("abc@gmail.", False),
    ("abc@@gmail.com", False),
    ("abc gmail@gmail.com", False)
]

print("EMAIL DFA TEST RESULTS")
print("----------------------")

for email, expected in test_cases:
    result = validate_email(email)

    if result == expected:
        print(email, ":", "PASS")
    else:
        print(email, ":", "FAIL")
