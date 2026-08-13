# Lab 1 — Foundations of Unit Testing with pytest

Software Testing and Validation, Addis Ababa University.

This bundle accompanies the Lab 1 manual. It contains a small system
under test, a starter test file for you to complete, and the instructor
solution.

## Setup

    python -m venv .venv
    source .venv/bin/activate        # on Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run the tests

From the project root:

    pytest -v                # runs your work in tests/
    pytest solution -v       # runs the instructor solution

## Structure

    src/            the system under test
      calculations.py     is_leap_year, grade, classify_triangle, buggy_max
      bank_account.py     the BankAccount class
    tests/          complete the TODOs here
      test_starter.py
    solution/       the full instructor solution
      test_calculations.py
      test_bank_account.py

## What to submit

Your completed tests/test_starter.py and a short answer to the Part C
question about error, fault and failure. See the lab manual for detail.
