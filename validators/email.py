
from automata.dfa import DFA

# Character categories
LETTER = "L"
DIGIT = "D"
DOT = "."
AT = "@"
UNDERSCORE = "_"
HYPHEN = "-"
OTHER = "O"

alphabet = {
    LETTER, DIGIT, DOT, AT,
    UNDERSCORE, HYPHEN, OTHER
}

# DFA states
states = {
    "q0", "q1", "q2", "q3",
    "q4", "q5", "q6", "q7"
}

# Transition rules
transitions = {
    # Username
    ("q0", LETTER): "q1",
    ("q0", DIGIT): "q1",

    ("q1", LETTER): "q1",
    ("q1", DIGIT): "q1",
    ("q1", DOT): "q2",
    ("q1", UNDERSCORE): "q2",
    ("q1", HYPHEN): "q2",
    ("q1", AT): "q3",

    ("q2", LETTER): "q1",
    ("q2", DIGIT): "q1",

    # Domain
    ("q3", LETTER): "q4",
    ("q3", DIGIT): "q4",

    ("q4", LETTER): "q4",
    ("q4", DIGIT): "q4",
    ("q4", HYPHEN): "q5",
    ("q4", DOT): "q6",

    ("q5", LETTER): "q4",
    ("q5", DIGIT): "q4",

    # Email extension
    ("q6", LETTER): "q7",

    ("q7", LETTER): "q7"
}

# Starting and accepting states
start_state = "q0"
final_states = {"q7"}

# Create DFA
email_dfa = DFA(
    states,
    alphabet,
    transitions,
    start_state,
    final_states
)


# Classify email characters
def classify_email(email):
    symbols = []

    for char in email:
        if char.isalpha() and char.isascii():
            symbols.append(LETTER)
        elif char.isdigit() and char.isascii():
            symbols.append(DIGIT)
        elif char == ".":
            symbols.append(DOT)
        elif char == "@":
            symbols.append(AT)
        elif char == "_":
            symbols.append(UNDERSCORE)
        elif char == "-":
            symbols.append(HYPHEN)
        else:
            symbols.append(OTHER)

    return symbols


# Validate email
def validate_email(email):
    symbols = classify_email(email)
    return email_dfa.validate(symbols)
