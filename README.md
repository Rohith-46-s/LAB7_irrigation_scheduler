# L6_L7_37 — Irrigation Scheduler

Lab 7: Fuzz Testing for Input Validation Bugs

## About

An advanced Python-based module designed to parse irrigation schedules, validate zone input parameters, and compute water usage metrics. This lab explores **property-based fuzz testing** using the **Hypothesis** library to uncover edge-case bugs, handle unexpected data streams, and enforce defensive programming practices.

---

## Files

| File | Description |
|------|-------------|
| `irrigation_scheduler.py` | Core application script featuring robust input validation and error-handling logic. |
| `test_irrigation_scheduler.py` | Property-based fuzz testing suite built with `pytest` and `Hypothesis`. |

---

## Learning Outcomes

* Understand the core principles and methodologies of dynamic fuzz testing.
* Apply property-based testing strategies to automatically discover edge-case input bugs.
* Detect exceptions, crashes, and malformed data handling (e.g., `None`, empty lists, unexpected types).
* Improve code robustness and reliability through strict defensive programming.

---

## Getting Started & Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Rohith-46-s/LAB7_irrigation_scheduler.git
   cd LAB7_irrigation_scheduler/lab7
   ```

2. **Install Dependencies:**

   Ensure you have `pytest` and `hypothesis` installed in your Python environment:

   ```bash
   python -m pip install hypothesis pytest
   ```

## Running the Application

Execute the core script to run pre-defined schedules and water calculation test cases:

```bash
python irrigation_scheduler.py
```

## Running the Fuzz Tests

Run the property-based test suite using `pytest` to automatically verify data invariants across hundreds of randomized input combinations:

```bash
python -m pytest test_irrigation_scheduler.py
``` 