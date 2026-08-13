"""A small stateful class you will test in Lab 1.

The account demonstrates preconditions, state changes and error
handling, which map onto the test case anatomy covered in Unit 1.
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""


class BankAccount:
    """A minimal bank account supporting deposits and withdrawals."""

    def __init__(self, opening_balance: float = 0.0) -> None:
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self._balance = float(opening_balance)

    @property
    def balance(self) -> float:
        """The current balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Add a positive ``amount`` to the balance."""
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove a positive ``amount`` from the balance if funds allow.

        Raises ``ValueError`` if the amount is not positive, and
        ``InsufficientFundsError`` if it exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("insufficient funds")
        self._balance -= amount
