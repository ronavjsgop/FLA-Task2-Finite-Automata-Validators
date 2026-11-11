
from automata.dfa import DFA

# Define states
states = {"q0", "q1", "q2", "q3", "q4", "DEAD"}

# Define alphabet
alphabet = set("0123456789")

# Define transitions
transitions = {}

# Four digit transitions
for digit in alphabet:
    transitions[("q0", digit)] = "q1"
    transitions[("q1", digit)] = "q2"
    transitions[("q2", digit)] = "q3"
    transitions[("q3", digit)] = "q4"
    transitions[("q4", digit)] = "DEAD"
    transitions[("DEAD", digit)] = "DEAD"

# Starting state
start_state = "q0"

# Accepting state
final_states = {"q4"}

# Create DFA
atm_dfa = DFA(
    states,
    alphabet,
    transitions,
    start_state,
    final_states
)

# Validate ATM PIN
def validate_atm_pin(pin):
    return atm_dfa.validate(pin)
