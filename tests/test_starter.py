"""Starter tests for Lab 1.

Complete each TODO, then run the whole file from the project root with:

    pytest -v

Give every test a name that describes the behaviour it checks. A good
test name reads like a sentence, for example test_deposit_increases_balance.
"""

import pytest

from src.calculations import is_leap_year, grade, classify_triangle, buggy_max
from src.bank_account import BankAccount, InsufficientFundsError


# ---------------------------------------------------------------------------
# Part A. Warm up.
# This test should already pass once pytest is installed. Run it to confirm
# your environment is working before you go any further.
# ---------------------------------------------------------------------------
def test_environment_is_ready():
    assert 2 + 2 == 4


# ---------------------------------------------------------------------------
# Part B. The test case anatomy.
# A deposit should increase the balance. Fill in the expected result.
# ---------------------------------------------------------------------------
def test_deposit_increases_balance():
    account = BankAccount(100.0)      # precondition
    account.deposit(50.0)             # input / action
    assert account.balance == 150.0   # expected result


# ---------------------------------------------------------------------------
# Part C. Reveal the planted fault in buggy_max.
# Choose inputs for which the fault produces a wrong result, so that this
# test FAILS. A failing test here is the correct outcome: it is how the
# fault becomes a visible failure.
# ---------------------------------------------------------------------------
def test_buggy_max_reveals_the_fault():
    assert buggy_max(1, 2) == 2   # buggy_max returns 1 (the first arg), but the correct max is 2


# ---------------------------------------------------------------------------
# Part D. Equivalence partitioning for is_leap_year.
# One partition is done for you. Add one test for each remaining partition.
# ---------------------------------------------------------------------------
def test_leap_year_divisible_by_4_not_100():
    assert is_leap_year(2024) is True


def test_leap_year_divisible_by_100_not_400():
    assert is_leap_year(1900) is False


def test_leap_year_divisible_by_400():
    assert is_leap_year(2000) is True


def test_leap_year_not_divisible_by_4():
    assert is_leap_year(2023) is False


# ---------------------------------------------------------------------------
# Part E. Boundary value analysis for grade.
# Test the values on and just below each boundary, plus the invalid range.
# ---------------------------------------------------------------------------
def test_grade_boundaries():
    assert grade(90) == "A"
    assert grade(89) == "B"
    assert grade(80) == "B"
    assert grade(79) == "C"
    assert grade(70) == "C"
    assert grade(69) == "D"
    assert grade(60) == "D"
    assert grade(59) == "F"
    assert grade(100) == "A"
    assert grade(0) == "F"


def test_grade_invalid_raises_value_error():
    with pytest.raises(ValueError):
        grade(-1)
    with pytest.raises(ValueError):
        grade(101)


# ---------------------------------------------------------------------------
# Part F. Challenge: design a suite for classify_triangle.
# One case is done for you. Cover isosceles, scalene and at least two
# different kinds of invalid input.
# ---------------------------------------------------------------------------
def test_classify_triangle_equilateral():
    assert classify_triangle(3, 3, 3) == "equilateral"


def test_classify_triangle_isosceles():
    assert classify_triangle(5, 5, 3) == "isosceles"


def test_classify_triangle_scalene():
    assert classify_triangle(3, 4, 5) == "scalene"


def test_classify_triangle_invalid_non_positive_side():
    assert classify_triangle(0, 4, 5) == "invalid"


def test_classify_triangle_invalid_triangle_inequality():
    assert classify_triangle(1, 2, 10) == "invalid"
