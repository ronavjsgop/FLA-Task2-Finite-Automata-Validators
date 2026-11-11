# Finite Automata for Real-Time Applications

## FLA Task 2 – Designing Automata for Real-Time Applications

A project demonstrating the practical application of **Finite Automata (DFA)** in real-world validation systems. This project implements three validators: Password Verification, Email Format Validation, and ATM PIN Verification.

## 🌐 Live Website

**[Visit the Finite Automata Validator Website](https://ronavjsgop.github.io/FLA-Task2-Finite-Automata-Validators/)**

## 📌 Project Overview

Finite Automata are mathematical models used to recognize patterns and validate input strings. This project demonstrates how Deterministic Finite Automata (DFA) can be used to validate different types of user inputs.

The project includes:

1. **Password Verification System** – Checks password length and verifies uppercase letters, lowercase letters, digits, and special characters.
2. **Email Format Validator** – Checks whether an email address follows the defined email format.
3. **ATM PIN Verification System** – Accepts exactly four numeric digits as a valid ATM PIN.

## 🎯 Objectives

- Understand the practical applications of Finite Automata.
- Design DFA state diagrams for real-time applications.
- Define alphabets, states, transitions, start states, and final states.
- Implement automata-based validation using Python.
- Test valid and invalid input strings.
- Demonstrate the working of automata through a web interface.

## 🛠️ Technologies Used

- Python
- HTML
- CSS
- JavaScript
- Git and GitHub
- GitHub Pages

## 📂 Project Structure

```text
FLA-Task2-Finite-Automata-Validators/
│
├── automata/
│   └── dfa.py
│
├── validators/
│   ├── password.py
│   ├── email.py
│   └── atm_pin.py
│
├── tests/
│   ├── test_password.py
│   ├── test_email.py
│   └── test_atm_pin.py
│
├── docs/
│   ├── diagrams/
│   │   ├── password.svg
│   │   ├── email.svg
│   │   └── atm_pin.svg
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Applications and Validation Rules

### 1. Password Verification System

The password validator checks whether a password satisfies the following conditions:

- Minimum length: 8 characters.
- Maximum length: 16 characters.
- At least one uppercase letter.
- At least one lowercase letter.
- At least one digit.
- At least one special character.
- Spaces are not allowed.

Example:

| Input | Result |
|---|---|
| `Hello@123` | Valid |
| `Welcome@1` | Valid |
| `hello123` | Invalid |
| `HELLO@123` | Invalid |

### 2. Email Format Validator

The email validator checks whether an email follows the defined format.

- Must contain a valid local part.
- Must contain exactly one `@` separator.
- Must contain a domain name.
- Must have a valid domain extension.
- Invalid spaces and misplaced symbols are rejected.

Example:

| Input | Result |
|---|---|
| `student@gmail.com` | Valid |
| `abc@yahoo.in` | Valid |
| `@gmail.com` | Invalid |
| `abc@gmail` | Invalid |

### 3. ATM PIN Verification System

The ATM PIN validator checks whether the entered PIN contains exactly four digits.

- Only numeric digits are allowed.
- Exactly four digits must be entered.
- Inputs with fewer or more than four digits are rejected.

Example:

| Input | Result |
|---|---|
| `1234` | Valid |
| `5678` | Valid |
| `123` | Invalid |
| `12345` | Invalid |

## ▶️ How to Run the Project

### Run Python Validators

Make sure Python is installed on your computer.

Open the project folder in VS Code and run these commands in the terminal:

**Password Validator**
```bash
python -m tests.test_password
```

**Email Validator**
```bash
python -m tests.test_email
```

**ATM PIN Validator**
```bash
python -m tests.test_atm_pin
```

### Run the Website

1. Open the `docs` folder.
2. Open `index.html` in Google Chrome or another web browser.
3. Select the required validator.
4. Enter an input string.
5. Click the Validate button.
6. View the validation result and transition information.

You can also access the website directly using the live website link above.

## 🧪 Testing

Each application includes valid and invalid test cases to verify the correctness of the validation system.

The test modules are available in the `tests/` directory.

## 📖 Limitations of Finite Automata

- Finite Automata have a limited number of states.
- They cannot remember unlimited information.
- They cannot recognize non-regular languages.
- Complex validation rules may require additional states or more powerful computational models.

## 🏁 Conclusion

This project demonstrates how Deterministic Finite Automata can be applied to practical validation problems such as password verification, email validation, and ATM PIN verification.

It provides a basic understanding of automata theory through Python implementation, state diagrams, transition logic, and a web-based interface.

## 👨‍💻 Project Information

**Subject:** Formal Languages and Automata Theory (FLA)  
**Project:** Task 2 – Designing Automata for Real-Time Applications  
**Repository:** [GitHub Repository](https://github.com/ronavjsgop/FLA-Task2-Finite-Automata-Validators)  
**Live Demo:** [GitHub Pages Website](https://ronavjsgop.github.io/FLA-Task2-Finite-Automata-Validators/)
