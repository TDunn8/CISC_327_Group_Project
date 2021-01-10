# R1 /Login
### R1.1 - If the user hasn't logged in, show the login page
Actions:
* open /logout
* open /login
* validate that the page contains 'Log In' text

### R1.2 - the login page has a message that by deafault says 'please login'
Actions:
* open /logout
* open /login
* validate that the page contains 'please login' text

### R1.3 - If the user has logged in, redirect to the user profile page
Mocking:
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login
* enter test_user email into #email element
* enter test_user password into #password element
* click submit element
* open /login
* validate that the page contains the welcome header

### R1.4 The login page provides a login form which requsts two fields: email and passwords
Actions:
* open /logout
* open /login
* validate that the page contains email input field
* validate that the page contains password input field

### R1.5 - The login form can be submitted as a POST request to the current URL (/login)

Mocking:
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login 
* enter test_user email into #email element
* enter test_user password into #password element
* click submit element
* verify the url ends in /login

### R1.6 - Email and password both cannot be empty
Mocking: 
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login
* enter test_user email into #email element
* click submit element
* validate page contains incorrect format message
* enter test_user password into #password element
* click submit element
* validate page contains incorrect format message


### R1.7 - Email has to follow addr-spec defined in RFC 5322
Mocking: 
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login
* enter 'test@test' into #email element
* enter test_user password into #password element
* click submit element
* validate that the page contains incorrect format message
* enter 'testtest.com' into #email element
* enter test_user password into #password element
* click submit element
* validate page contains incorrect format message


### R1.8 - Password has to meet the required complexity
Mocking: 
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login
* enter test_user email into #email element
* enter 'T_st1' password into #password element
* click submit element
* validate that the page contains incorrect format message
* enter test_user email into #email element
* enter 'test_1' password into #password element
* click submit element
* validate that the page contains incorrect format message
* enter test_user email into #email element
* enter 'TEST_1' password into #password element
* click submit element
* validate that the page contains incorrect format message
* enter test_user email into #email element
* enter 'Test11' password into #password element
* click submit element
* validate that the page contains incorrect format message

### R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect'
Verified in R1.6, R1.7, R1.8

### R1.10 - If email/password are correct, redirect to /
Verified in R1.3

### R1.11 - Otherwise, redirect to /login and show message 'email/password combination incorrect'
Mocking: 
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login
* enter 'wrong@email.com' into #email element
* enter test_user password into #password element
* click submit element
* validate that the page contains incorrect combination message
* enter test_user email into #email element
* enter 'Wrong_pass1' password into #password element
* click submit element
* validate that the page contains incorrect combination message


# R2 /register
### R2.1 - If the user has logged in, redirect back to the user profile page /
Mocking:
* Mock backend.get_user to return test_user

Actions:
* open /logout
* open /login
* enter test_user email into #email element
* enter test_user password into #password element
* click submit element
* open user profile page /
* validate page #welcome-header is 'welcome user.name'

### R2.2 - otherwise, show the user registration page
Actions:
* open /logout
* validate the page element h1 reads 'register'

### R2.3 - the registration page shows a registration form requiesting: email, user name, password, password2

Actions:
* open /register
* validate that the class #form-control contains elements email, user name, password, password2

### R2.4 The registration form can be submitted as a POST request to the current URL (/register)

Actions:
* open /register
* click submit element
* validate url ends in /register


### R2.5 - Email, password, password2 all have to satisfy the same required as defined in R1
Actions:
* See R1.6 - R1.8

### R2.6 - Password and password2 have to be exactly the same

Actions:
* open /register
* enter valid test email into #email element
* enter valid test password into #password element
* enter different password into #password2 element
* click submit element
* validate page contains 'passwords must match' message


### R2.7 - User name has to be non-empty, alphanumberic-only, and space allowed only if it is not the first or last character

Actions:
* open /register
* enter valid test email into #email element
* enter valid password into #password element
* enter same password into #passowrd2 element
* click submit element
* validate that the page contains incorrect format message
* enter 'namehasa1' into #username element
* click submit element
* validate page contains incorrect format message
* enter ' testuser' into #username element
* click submit element
* validate page contains incorrect format message
* enter 'testuser ' into #username element
* validate page contains incorrect format message


### R2.8 - User name has to be longer than 2 characters and less than 20 characters

Actions:
* open /register
* enter valid test email into #email element
* enter valid password into #password element
* enter same password into #passowrd2 element
* enter 'ab' into #username element
* click submit element
* validate page contains incorrect format message
* enter 'abcdefghijklmnopqrstuvwxyz' into #username element
* click submit eleent
* validate page contaiins incorrect format message

### R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format
Verified in R2.6, R2.7, R2.8

### R2.10 - If the email already exists, show message 'this email has been ALREADY used'
Mocking: 
* Mock backend.get_user to return test_user

Actions:
* enter test_user email into #email element
* enter test_user password into #password element
* enter test_user password into #passowrd2 element
* enter valid username into #username element
* click submit element
* validate page contains 'email already used' message

### R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page

Actions:
* enter valid new email into #email element
* enter valid password into #password element
* enter valid password into #passowrd2 element
* enter valid username into #username element
* click submit element
* validate that the page contains the login message
* validate the user has a balaance of 5000


| Specification | Test case ID | Purpose |
|:-:|-|:-:|
| R3 | / | |
| If the user is not logged in, redirect to login page | R3.1.1 | Check if user is redirected to /login when not logged in |
| This page shows a header 'Hi {}'.format(user.name) | R3.2.1 | Check if there is a header 'Hi {}'.format(user.name) when user logged in |
| This page shows user balance | R3.3.1 | Check if the user balance is visible when logged in |
| This page shows a logout link, pointing to /logout | R3.4.1 | Check if user is redirected to /logout if logout link is clicked |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.1 | Check if any expired tickets are shown |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.2 | Check if page shows quantity for each ticket that is not expired |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.3 | Check if page shows the owners email for each ticket that is not expired |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.4 | Check if page shows each ticket's price if not expired |
| This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date | R3.6.1 | Check if form fails when name is invalid |
| This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date | R3.6.2 | Check if form fails when quantity is invalid |
| This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date | R3.6.3 | Check if form fails when price is invalid |
| This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date | R3.6.4 | Check if form fails when expiration date is invalid |
| This page contains a form that a user can buy new tickets. Fields: name, quantity | R3.7.1 | Check if purchase fails when name is invalid |
| This page contains a form that a user can buy new tickets. Fields: name, quantity | R3.7.2 | Check if purchase fails when quantity is invalid |
| This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date | R3.8.1 | Check if update fails when name is invalid |
| This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date | R3.8.2 | Check if update fails when quantity is invalid |
| This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date | R3.8.3 | Check if update fails when price is invalid |
| This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date | R3.8.4 | Check if update fails when expiration date is invalid |
| The ticket-selling form can be posted to /sell | R3.9.1 | Check if ticket-selling form is posted on /sell if all fields are valid |
| The ticket-buying form can be posted to /buy | R3.10.1 | Check if ticket-buying form is posted on /buy if all fields are valid |
| The ticket-update form can be posted to /update | R3.11.1 | Check if ticket-update form is posted on /update if all fields are valid |
|  |  |  |
| R4 | /sell |  |
| The name of the ticket has to be alphanumeric-only | R4.1.1 | Check if the selling actions succeed when the ticket names is alphanumeric-only |
| The name of the ticket has to be alphanumeric-only | R4.1.2 | Check if the selling actions fail when the ticket names contains special characters |
| The name of the ticket is no longer than 60 characters | R4.2.1 | Check if selling actions fails when ticket name is longer than 60 characters |
| The name of the ticket is no longer than 60 characters | R4.2.2 | Check if selling actions succeed when ticket name is 60 characters or less |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R4.3.1 | Check if selling actions fail if ticket quantity is 0 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R4.3.2 | Check if selling actions fail if ticket quantity is greater than 100 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R4.3.3 | Check if selling actions succeed if ticket quantity is between 1 and 100 |
| Price has to be of range [10, 100] | R4.4.1 | Check if selling actions fail if price is less than 10 |
| Price has to be of range [10, 100] | R4.4.2 | Check if selling actions fail if price is greater than 100 |
| Price has to be of range [10, 100] | R4.4.3 | Check if selling actions succeeds if price is between 10 and 100 |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R4.5.1 | Check if selling actions fail if date is not in the format YYYYMMDD |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R4.5.2 | Check if selling actions succeed if date is in the format YYYYMMDD |
| For any errors, redirect back to / and show an error message | R4.6.1 | Check if error redirects back to / |
| For any errors, redirect back to / and show an error message | R4.6.2 | Check if / shows error mesage when redirected |
| The added new ticket information will be posted on the user profile page | R4.7.1 | Check if new ticket information is posted on the user profile page |
| The name of the tickets has to contain at least 6 characters | R4.8.1 | Check if posting new ticket fails if ticket name is less than 6 characters |
| The name of the tickets has to contain at least 6 characters | R4.8.2 | Check if posting new ticket succeeds if ticket name is 6 characters or more |
| The new tickets must not be expired | R4.9.1 | Check if posting new ticket fails if ticket is expired |
| The new tickets must not be expired | R4.9.2 | Check if posting new ticket succeeds if ticket is not expired |
|  |  |  |

### R5.1.1 The name of the ticket has to be alphanumeric-only and Space allowed only if it is not the first or the last character - positive
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter 50 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows successful
- open /logout


### R5.1.1 The name of the ticket has to be alphanumeric-only - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "%#&*?" into element #update_name
- enter 50 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Name must be numbers and letters only"
- open /logout


### R5.1.2 Space allowed only if it is not the first or the last character. - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " name " into element #update_name
- enter 50 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Name must not start or end with space"
- open /logout


### R5.2.1 The name of the ticket is no longer than 60 characters - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter 61 character name into element #update_name
- enter 50 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Name must be less than or equal to 60 characters"
- open /logout


### R5.3.1 The quantity of the ticket has to be more than 0 - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter -10 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Quantity must be greater than 0"
- open /logout


### R5.3.2 The quantity of the ticket has to be less than or equal to 100 - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter 105 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Quantity must be less than 101"
- open /logout


### R5.4.1  Price must be greater than or equal to 10 - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter 50 into #update_quantity
- enter 9.50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Price must be 10 or greater"
- open /logout


### R5.4.2  Price must be less than or equal to 100 - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter 50 into #update_quantity
- enter 100.50 into #update_price
- enter 20200930 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Price must be 100 or less"
- open /logout


### R5.4.2  Date must be given in YYYYMMDD format - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter 50 into #update_quantity
- enter 50 into #update_price
- enter 09302020 into #update_date
- enter test_ticket's name into #name
- click element #update_submit
- validate that the #update_message element shows "Date needs different format (YYYYMMDD)"
- open /logout


### R5.5.1 Ticket of the given name must exist - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "Proper name" into element #update_name
- enter 50 into #update_quantity
- enter 50 into #update_price
- enter 20200930 into #update_date
- enter "fake ticket name" into #name
- click element #update_submit
- validate that the #update_message element shows "Ticket doesn't exist"
- open /logout


### R5.6.1 For any errors, redirect to / and show an error message
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " &*^ " into element #update_name
- enter 500 into #update_quantity
- enter 500 into #update_price
- enter 30121998 into #update_date
- enter " ?!@ " name into #name
- click element #update_submit
- validate #update_message as error message
- click element #message_received on #update_message
- validate that page is /
- open /logout





### R6.1.1 The name of the ticket has to be alphanumeric-only and Space allowed only if it is not the first or the last character - positive
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter test_ticket's name into element #buy_name
- enter test_ticket's quantity into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows successful
- open /logout


### R6.1.2 The name of the ticket has to be alphanumeric-only - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "%^&" into element #buy_name
- enter test_ticket's quantity into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Ticket name must be numbers or letters"
- open /logout


### R6.1.3 Space not allowed as first or last character of ticket name - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " name " into element #buy_name
- enter test_ticket's quantity into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Ticket name must not start or end with space"
- open /logout


### R6.2.1 The name of the ticket is no longer than 60 characters - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter 61 character name into element #buy_name
- enter test_ticket's quantity into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Ticket name must be less than 60 characters"
- open /logout


### R6.3.1 The quantity of the ticket has to be more than 0 - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter test_ticket's name into element #buy_name
- enter 0 into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Buy quantity must be greater than 0"
- open /logout


### R6.3.2 The quantity of the tickets must be less than or equal to 100 - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter test_ticket's name into element #buy_name
- enter 101 into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Buy quantity must be less than or equal to 100"
- open /logout


### R6.4.1 The ticket name must exist in database
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "nothing" into element #buy_name
- enter test_ticket's quantity into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Ticket does not exist"
- open /logout


### R6.4.2  Quantity must be greater than buy quantity requested - negative
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter test_ticket's name into element #buy_name
- enter 99 into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Not enough tickets"
- open /logout


### R6.5.1 The user has more balance than the ticket price
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter test_ticket's name into element #buy_name
- enter test_ticket's quantity into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows "Balance too low"
- open /logout


### R6.6.1 For any errors

Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_ticket to return a test_ticket instance
Actions:
- open /logout to handle and logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " &*% " into element #buy_name
- enter 101 into #buy_quantity
- click element #buy_submit
- validate that the #buy_message element shows error message
- click element #message_received on #update_message
- validate that page is /
- open /logout


### R7 Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages
Mocking:
- Mock backend.get_user to return a test_user instance
Actions:
- open /logout to handle any logged-in sessions that exist
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- click element input[type="logout"]
- validate that user is logged out
- validate that the user cannot open /

### R8 Request nonexistent page
Actions:
- open /logout to handle any logged-in sessions that exist
- attempt to open nonexistent /something page
- validate 404 error
