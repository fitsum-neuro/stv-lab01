# Part C — Error, Fault and Failure Analysis of `buggy_max`

The **error** (human mistake) was the programmer's incorrect assumption that the first argument `a` is always the larger value, leading them to write a return statement that ignores `b` entirely.

The **fault** (defect in the code) is on line 71 of `calculations.py`: the function body is `return a`, which discards the second argument instead of comparing both values and returning the larger one.

The **failure** (observable wrong behaviour) occurs when `b > a`. For example, calling `buggy_max(1, 2)` returns `1` instead of the correct answer `2`. The fault is **reached** whenever the function is called, the internal state is **infected** because the comparison with `b` never takes place, but the failure only **propagates** to a visible wrong output when `b` is strictly greater than `a` — if `a >= b`, the faulty code accidentally returns the correct result.
