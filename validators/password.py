
from automata.dfa import DFA

# Password character categories
UPPER = "U"
LOWER = "L"
DIGIT = "D"
SPECIAL = "S"
OTHER = "O"

# Convert each character into a category
def classify_password(password):
    symbols = []

    for char in password:
        if char.isupper():
            symbols.append(UPPER)
        elif char.islower():
            symbols.append(LOWER)
        elif char.isdigit():
            symbols.append(DIGIT)
        elif char in "!@#$%^&*()-_=+[]{};:,.?/":
            symbols.append(SPECIAL)
        else:
            symbols.append(OTHER)

    return symbols


# Create DFA states
# Each state contains (length, requirements_met)
DEAD = "DEAD"

states = {
    (length, mask)
    for length in range(17)
    for mask in range(16)
}

states.add(DEAD)

alphabet = {UPPER, LOWER, DIGIT, SPECIAL, OTHER}

transitions = {}

# Build DFA transitions
for state in states:
    if state == DEAD:
        for symbol in alphabet:
            transitions[(DEAD, symbol)] = DEAD
        continue

    length, mask = state

    for symbol in alphabet:
        if symbol == OTHER or length == 16:
            transitions[(state, symbol)] = DEAD
        else:
            new_mask = mask

            if symbol == UPPER:
                new_mask |= 1
            elif symbol == LOWER:
                new_mask |= 2
            elif symbol == DIGIT:
                new_mask |= 4
            elif symbol == SPECIAL:
                new_mask |= 8

            transitions[(state, symbol)] = (length + 1, new_mask)


# Define accepting states
final_states = {
    (length, 15)
    for length in range(8, 17)
}

# Create password DFA
password_dfa = DFA(
    states,
    alphabet,
    transitions,
    (0, 0),
    final_states
)


# Validate password
def validate_password(password):
    symbols = classify_password(password)
    return password_dfa.validate(symbols)
