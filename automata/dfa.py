
class DFA:

    def __init__(self, states, alphabet, transitions, start_state, final_states):

        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def validate(self, input_string):

        current_state = self.start_state

        for symbol in input_string:

            if symbol not in self.alphabet:
                return False

            if (current_state, symbol) not in self.transitions:
                return False

            current_state = self.transitions[(current_state, symbol)]

        return current_state in self.final_states
    
