# AI Code Review Assignment (Python)

## Candidate
- Name:Ayşenur Oğuz
- Approximate time spent:60 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Division by total orders instead of valid orders - calculates wrong average
- ZeroDivisionError when list is empty or all orders cancelled

### Edge cases & risks
- KeyError if "status" or "amount" keys missing
- No type checking - crashes on None or non-dict values
- Negative amounts not validated

### Code quality / design issues
- Uses `order["key"]` instead of safer `.get()` method
- No docstring
- No input validation

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track valid order count separately
- Add checks for empty list and zero valid count
- Use `.get()` for safe dictionary access
- Add type and value validation

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Empty lists, all cancelled orders, missing keys, None values, negative amounts. These cover the main failure modes.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Says "correctly excludes" but divides by ALL orders, not just valid ones
- Doesn't mention any error handling issues
- Claims correctness when the math is wrong

### Rewritten explanation
Calculates average order value for non-cancelled orders. Filters out cancelled orders from the sum and count to ensure accurate average. Handles edge cases like empty input and missing dictionary keys safely. 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification: Wrong average calculation is a critical bug. Empty list crashes the function. These aren't style issues.
- Confidence & unknowns: High confidence - bugs are straightforward to reproduce. Could return None instead of 0 for empty input depending on requirements.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- TypeError when email is not a string (no type check)

### Edge cases & risks
- Only checks for "@" - accepts invalid formats like "@", "@@", "@test.com", "test@"
- No domain validation (no .com, .org check)
- Empty strings not explicitly handled

### Code quality / design issues
- Validation is too basic for "valid email"
- No docstring

## 2) Proposed Fixes / Improvements
### Summary of changes
- Add type checking with isinstance
- Split by "@" and verify exactly one @ symbol
- Check both parts (local and domain) are non-empty
- Verify domain has at least one dot

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Valid emails vs obviously invalid ones ("@", "@@", "test@"), non-string inputs, empty list. Want to ensure basic structure validation works without being too strict.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- "Valid email addresses" is misleading - only checks for "@"
- Not "safely" - crashes on non-strings
- Doesn't explain what makes an email valid

### Rewritten explanation
Counts emails with basic valid structure: one "@" symbol with non-empty text before and after, and domain containing a dot. Skips non-string values and malformed entries.


## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification: Calling "@" a valid email is wrong. Type error will crash in production. Need basic validation.
- Confidence & unknowns: High confidence on issues. Could use regex for more thorough validation but this is reasonable for basic filtering. 

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Same as Task 1 - divides by len(values) but only sums non-None values
- ZeroDivisionError on empty list

### Edge cases & risks
- float() raises ValueError on invalid strings like "abc"
- TypeError on lists, dicts, other non-numeric types
- No error handling around type conversion

### Code quality / design issues
- No try-except for conversions
- No docstring 

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only successfully converted values
- Wrap float() in try-except
- Check for empty list and zero valid count
- Skip unconvertible values instead of crashing 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

None values, numeric strings, invalid strings, mixed types, empty list. Main concern is handling type diversity in real sensor data.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Not "accurate" - wrong denominator
- Doesn't "safely handle" mixed types - crashes on invalid strings
- Overpromises on capabilities 

### Rewritten explanation
Calculates average of numeric measurements, filtering out None values and invalid data. Converts values to float safely and handles type errors. Returns 0 if no valid measurements exist.

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification: Incorrect average and missing error handling are critical issues for data processing code.
- Confidence & unknowns: Very confident. Could debate whether to return 0 or None for no valid data.
