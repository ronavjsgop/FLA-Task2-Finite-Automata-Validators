
from validators.password import validate_password

# Valid and invalid password examples
test_cases = [
    ("Abc@1234", True),
    ("Hello@123", True),
    ("Pass#2026", True),
    ("Test@1234A", True),
    ("A1b@cdef", True),

    ("abc12345", False),
    ("ABC@1234", False),
    ("Abc@123", False),
    ("Abcdefgh", False),
    ("Abc @1234", False)
]

print("PASSWORD DFA TEST RESULTS")
print("--------------------------")

for password, expected in test_cases:
    result = validate_password(password)

    if result == expected:
        print(password, ":", "PASS")
    else:
        print(password, ":", "FAIL")
