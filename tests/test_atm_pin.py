
from validators.atm_pin import validate_atm_pin

test_cases = [
    ("1234", True),
    ("5678", True),
    ("0000", True),
    ("9876", True),
    ("2468", True),

    ("123", False),
    ("12345", False),
    ("12ab", False),
    ("12@4", False),
    ("12 4", False)
]

print("ATM PIN DFA TEST RESULTS")
print("------------------------")

for pin, expected in test_cases:
    result = validate_atm_pin(pin)

    if result == expected:
        print(pin, ":", "PASS")
    else:
        print(pin, ":", "FAIL")
