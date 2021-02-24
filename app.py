from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_topping1 = request.args.get('topping1')
    users_topping2 = request.args.get('topping2')

    context = {
        'users_froyo_flavor': users_froyo_flavor,
        'users_topping1': users_topping1,
        'users_topping2': users_topping2
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
        <form action="/favorites_results" method="GET">
        What is your favorite color?
        <input type="text" name="color">
        </br>
        What are your favorite animal?
        <input type="text" name="animal">
        </br>
        What are your favorite city?
        <input type="text" name="city">
        </br>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_favorite_color = request.args.get('color')
    user_favorite_animal = request.args.get('animal')
    user_favorite_city = request.args.get('city')
    return f'Wow, I didn\'t know {user_favorite_color} {user_favorite_animal} lived in {user_favorite_city}'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
        <form action="/message_results" method="POST">
        Type your message here
        </br>
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form['message']
    user_message = sort_letters(message) 

    return f'Here is your secret message! {user_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    num1 = int(request.args.get('operand1'))
    num2 = int(request.args.get('operand2'))
    op_type = request.args.get('operation')
    answer = 0

    if op_type == "add":
        answer = num1 + num2
    elif op_type == "subtract":
        answer = num1 - num2
    elif op_type == "multiply":
        answer = num1 * num2
    elif op_type == "divide":
        answer = num1 / num2
    else:
        return False

    context = {
        'num1': num1,
        'num2': num2,
        'op_type': op_type,
        'answer': answer

    }
    return render_template('calculator_results.html', **context)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    users_name = request.args.get('users_name')

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')        

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = request.args.get('HOROSCOPE_PERSONALITIES')

    if horoscope_sign == "aries":
        HOROSCOPE_PERSONALITIES == 'aries'
    elif horoscope_sign == "taurus":
        HOROSCOPE_PERSONALITIES == 'taurus'
    elif horoscope_sign == "gemini":
        HOROSCOPE_PERSONALITIES == 'gemini'
    elif horoscope_sign == "cancer":
        HOROSCOPE_PERSONALITIES == 'cancer'
    elif horoscope_sign == "leo":
        HOROSCOPE_PERSONALITIES == 'leo'
    elif horoscope_sign == "virgo":
        HOROSCOPE_PERSONALITIES == 'virgo'
    elif horoscope_sign == "libra":
        HOROSCOPE_PERSONALITIES == 'libra'
    elif horoscope_sign == "scorpio":
        HOROSCOPE_PERSONALITIES == 'scorpio'
    elif horoscope_sign == "sagittarius":
        HOROSCOPE_PERSONALITIES == 'sagittarius'
    elif horoscope_sign == "capricorn":
        HOROSCOPE_PERSONALITIES == 'capricorn'
    elif horoscope_sign == "aquarius":
        HOROSCOPE_PERSONALITIES == 'aquarius'
    elif horoscope_sign == "pisces":
        HOROSCOPE_PERSONALITIES == 'pisces'


    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(0, 100)

    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'users_personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
