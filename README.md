# Debugging Challenge

## Instructions

You have TWO debugging tasks. Run each file and use the error messages to find and fix the bugs.

### Task 1: Code Errors (task1.py)
Just run the file to test. Fix each error as you encounter it, then run again.

### Task 2: Input and Conversion Errors (task2.py)
Run the file and enter values when prompted. Fix each error as you encounter it.

**When finished with task2:** Comment out `main()` at the bottom of the file before running pytest.

---

## Testing Your Fixes

Run pytest to check your work:
```
pytest -v
```

---

## For the Sub

Students should:
1. Start with task1.py - run it, see the error, fix it, run again
2. Move to task2.py - run it, enter values, see the error, fix it, repeat
3. When task2 is working, comment out `main()` at the bottom
4. Run `pytest -v` to verify all fixes

**Hints if students are stuck:**
- Task 1: Look for typos in variable names, missing pieces in f-strings
- Task 2: Remember `input()` always returns a string - use `int()` or `float()` to convert
