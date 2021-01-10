from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import re

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='Register')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


    if password != password2:
        error_message = "The passwords do not match"

    elif len(email) < 1:
        error_message = "Email format error"
        
    elif name.startswith((' ', '\t')):
        error_message = "Name format error"
        
    elif name.endswith((' ', '\t')):
        error_message = "Name format error"
    
    elif not name.isalnum():
        error_message = "Name format error"

    elif len(password) < 1:
        error_message = "Password is not strong enough"
        
    elif (not re.search(regex,email)):
        error_message = "Email format error"
    
    elif len(password) < 6:
        error_message = "Password is not strong enough"
        
    elif not any(x.isupper() for x in password):
        error_message = "Password is not strong enough"
        
    elif not any(x.islower() for x in password):
        error_message = "Password is not strong enough"
        
    elif not any(x.isalnum() for x in password):
        error_message = "Password is not strong enough"
        
    elif not (2<len(name)<20):
        error_message = "Name format error"
    else:
        user = bn.get_user(email)
        if user:
            error_message = "User exists"
        elif not bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (not re.search(regex,email)):
        return render_template('login.html', message='Email format error')
    
    elif len(email) < 1:
        return render_template('login.html', message='Email format error')

    elif len(password) < 1:
        return render_template('login.html', message='Email format error')
    
    elif len(password) < 6:
        return render_template('login.html', message='Email format error')
    
    elif not any(x.isupper() for x in password):
        return render_template('login.html', message='Email format error')
        
    elif not any(x.islower() for x in password):
        return render_template('login.html', message='Email format error')

    elif not any(x.isalnum() for x in password):
        return render_template('login.html', message='Email format error')

    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='Email format error')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/', methods=['GET'])
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)


@app.route('/sell',  methods=['POST'])
def sell_post():
    name = request.form.get('sell-name')
    quantity = int(request.form.get('sell-quantity'))
    price = int(request.form.get('sell-price'))
    expiration = request.form.get('sell-expirationDate')
    convertedDate = str(expiration)
    year = int(convertedDate[:4])
    month = int(convertedDate[4:6])
    day = int(convertedDate[6:])
    email = session['logged_in']
    user = bn.get_user(email)
    error_message = None

    if name.startswith((' ', '\t')):
        error_message='Name format error'

    elif name.endswith((' ', '\t')):
        error_message='Name format error'

    elif len(name) > 60:
        error_message='Name format error'

    elif quantity < 0 or quantity > 100:
        error_message='Quantity error'

    elif price < 10 or price > 100:
        error_message='Price error'

    elif len(expiration) != 8:
        error_message='Expiration date error'

    elif year < 2000 or year > 2100:
        error_message='Expiration date error'

    elif month < 1 or month > 12:
        error_message='Expiration date error'

    elif day < 1 or day > 31:
        error_message='Expiration date error'

    if error_message:
        tickets = bn.get_all_tickets()
        return render_template('index.html', tickets=tickets, user=user, sell_message=error_message)
    else:
        bn.add_ticket(name, quantity, price, expiration, email)
        return redirect('/')  

@app.route('/buy',  methods=['POST'])
def buy_post():
    name = request.form.get('buy-name')
    quantity = int(request.form.get('buy-quantity'))
    email = session['logged_in']
    user = bn.get_user(email)
    ticket = bn.get_ticket(name)
    error_message = None
    
    if ticket:
        if name.startswith((' ', '\t')):
            error_message='Name format error'

        elif name.endswith((' ', '\t')):
            error_message='Name format error'

        elif len(name) > 60:
            error_message='Name format error'
        
        elif quantity > 100 or quantity < 1:
            error_message ='Qauntity error'

        elif quantity > ticket.quantity:
            error_message = 'Quantity error'
        
        elif 1.4*ticket.price > user.balance:
            error_message = 'Insufficient funds'
    else:
        error_message = 'Ticket does not exist'
    
    
    if error_message:
        tickets = bn.get_all_tickets()
        return render_template('index.html', tickets=tickets, user=user, buy_message=error_message)
    else:
        bn.buy_ticket(name, quantity, user.email, ticket.price)
        return redirect('/')  

@app.route('/update',  methods=['POST'])  
def update_post():
    name = request.form.get('update-name')
    quantity = request.form.get('update-quantity')
    price = request.form.get('update-price')
    expirationDate = request.form.get('update-expirationDate')
    convertedDate = str(expirationDate)
    year = int(convertedDate[:4])
    month = int(convertedDate[4:6])
    day = int(convertedDate[6:])
    email = session['logged_in']
    user = bn.get_user(email)
    tickets = bn.get_all_tickets()

    if name.startswith((' ', '\t')):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Name format error")
        
    elif name.endswith((' ', '\t')):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Name format error")
    
    elif not name.isalnum():
        return render_template('index.html', user=user, tickets=tickets, update_message = "Name format error")
    
    elif len(name) > 60:
        return render_template('index.html', user=user, tickets=tickets, update_message = "Name format error")
    
    elif not (0 < quantity < 101):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Quantity must be between 0 and 100")
    
    elif not (10 <= price <= 100):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Price must be between 10 and 100")
    elif not (2000<year<2100):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Date format error")
    elif not (0<month<13):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Date format error")
    elif not (0<day<32):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Date format error")
    elif not (bn.check_ticket(name, quantity, price, expirationDate)):
        return render_template('index.html', user=user, tickets=tickets, update_message = "Ticket does not exist")
    else:
        return render_template('index.html', user=user, tickets=tickets, update_message = "Success")
    
