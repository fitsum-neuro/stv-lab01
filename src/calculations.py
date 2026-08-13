"""Functions under test for Lab 1.

These are the units you will design tests for. Most are correct
reference implementations. One function, ``buggy_max``, contains a
deliberate fault so that you can experience the error, fault and
failure chain from the lecture in practice.
"""


def is_leap_year(year: int) -> bool:
    """Return True if ``year`` is a leap year in the Gregorian calendar.

    A year is a leap year if it is divisible by 4, except that years
    divisible by 100 are not leap years unless they are also divisible
    by 400. For example 1996 and 2000 are leap years, while 1900 is not.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def grade(score: int) -> str:
    """Convert a numeric ``score`` in the range 0 to 100 to a letter grade.

    Bands: 90 to 100 gives A, 80 to 89 gives B, 70 to 79 gives C,
    60 to 69 gives D, and 0 to 59 gives F.

    Raises ``ValueError`` if the score is outside the range 0 to 100.
    """
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def classify_triangle(a: int, b: int, c: int) -> str:
    """Classify a triangle from its three side lengths.

    Returns one of ``"equilateral"``, ``"isosceles"``, ``"scalene"``
    or ``"invalid"``. A set of sides is invalid if any side is not
    positive, or if the triangle inequality does not hold (the sum of
    any two sides must exceed the third).
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"


def buggy_max(a: int, b: int) -> int:
    """Return the larger of two integers.

    NOTE FOR STUDENTS: this implementation contains a deliberate fault.
    In Part C you will write a test that reveals the failure, then
    explain the defect using the error, fault and failure vocabulary.
    """
    return a  # fault: the value of b is ignored entirely
