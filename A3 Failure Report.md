| Test #       | Purpose        | Problem  | Fix |
|:-------------:|:-------------:|:-----:|:---------:|
| R1.3  | Validate that a correct login works|frontend.py improperly flagged correct passwords as invalid | Fix frontend.py to properly validate passwords |
| R1.6/R2.7  | Validate error message when leaving login fields blank | html forms give a 'error blank field' popup instead of the expected error message| Change test case to validate that the login webpage is still open when field is left blank |
|R2|Use the registration page| frontend.py uses str.endsWith(), should be str.endswith()| Replace 'W' with 'w' |
|R2.11| If registration succeeds, open /login | Registration failed due to invalid password| Fix frontend.py to check for a single special character in password, instead of invalidating passwords with a special character  |
|R3 | Mocking test user | Email and password did not meet requirements | Update test user email to be in correct format and password to include uppercase, lowercase, number, and special character  |
