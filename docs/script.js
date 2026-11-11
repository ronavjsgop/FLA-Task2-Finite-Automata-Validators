
// =====================================
// 1. PASSWORD VERIFICATION DFA
// =====================================

function validatePassword() {
    const password = document.getElementById("passwordInput").value;
    const result = document.getElementById("passwordResult");
    const trace = document.getElementById("passwordTrace");

    let state = 0;

    const categories = {
        U: /[A-Z]/,
        L: /[a-z]/,
        D: /[0-9]/,
        S: /[^A-Za-z0-9\s]/
    };

    let seen = { U: false, L: false, D: false, S: false };
    let steps = ["Start: q0"];

    for (let char of password) {
        let category = null;

        for (let key in categories) {
            if (categories[key].test(char)) {
                category = key;
                break;
            }
        }

        if (category === null) {
            state = "DEAD";
        } else if (state !== "DEAD") {
            seen[category] = true;
            state = "q" + (
                (seen.U ? 1 : 0) +
                (seen.L ? 2 : 0) +
                (seen.D ? 4 : 0) +
                (seen.S ? 8 : 0)
            );
        }

        steps.push(char + " → " + state);

        if (state === "DEAD") break;
    }

    const valid =
        password.length >= 8 &&
        password.length <= 16 &&
        seen.U && seen.L && seen.D && seen.S &&
        state !== "DEAD";

    showResult(result, valid,
        valid ? "Password Accepted!" : "Password Rejected!");

    showTrace(trace, steps, "Final State: " + state);
}


// =====================================
// 2. EMAIL FORMAT VALIDATOR
// =====================================

function validateEmail() {
    const email = document.getElementById("emailInput").value;
    const result = document.getElementById("emailResult");
    const trace = document.getElementById("emailTrace");

    const pattern =
        /^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)*\.[A-Za-z]{2,}$/;

    const valid = pattern.test(email);

    let steps = ["Start: q0"];

    if (valid) {
        steps.push("Local part → q1");
        steps.push("@ symbol → q2");
        steps.push("Domain labels → q3");
        steps.push("Final extension → q4");
    } else {
        steps.push("Input does not match the required email pattern");
        steps.push("Final State: DEAD");
    }

    showResult(result, valid,
        valid ? "Email Accepted!" : "Email Rejected!");

    showTrace(trace, steps,
        valid ? "Final State: q4 (Accept)" : "Final State: DEAD (Reject)");
}


// =====================================
// 3. ATM PIN VERIFICATION DFA
// =====================================

function validatePIN() {
    const pin = document.getElementById("pinInput").value;
    const result = document.getElementById("pinResult");
    const trace = document.getElementById("pinTrace");

    let state = 0;
    let steps = ["Start: q0"];

    for (let digit of pin) {
        if (!/[0-9]/.test(digit) || state === "DEAD") {
            state = "DEAD";
        } else {
            state++;
            if (state > 4) state = "DEAD";
        }

        steps.push(digit + " → " + (state === "DEAD" ? "DEAD" : "q" + state));

        if (state === "DEAD") break;
    }

    const valid = /^[0-9]{4}$/.test(pin);

    showResult(result, valid,
        valid ? "ATM PIN Accepted!" : "ATM PIN Rejected!");

    showTrace(trace, steps,
        "Final State: " + (valid ? "q4 (Accept)" : "DEAD / Incomplete (Reject)"));
}


// =====================================
// COMMON RESULT AND TRACE FUNCTIONS
// =====================================

function showResult(element, valid, message) {
    element.textContent = message;
    element.className = valid ? "success" : "error";
}

function showTrace(element, steps, finalState) {
    element.className = "trace";
    element.innerHTML =
        "<strong>Transition Trace:</strong><br>" +
        steps.map(step => escapeHTML(step)).join("<br>") +
        "<br><br><strong>" + escapeHTML(finalState) + "</strong>";
}

function escapeHTML(text) {
    return text.replace(/[&<>"']/g, function (char) {
        return {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#039;"
        }[char];
    });
}
