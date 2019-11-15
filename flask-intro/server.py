"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['you are a poopie head', 'you suck', 'you are stuuuuupid']


@app.route("/")
def start_here():
    """Home page."""

    return """
      <!doctype html>
      <html>
        <a href="/hello">
          Hi! This is the home page.
        </a>
      </html>
      """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person"><br>
          Select your compliment 
            <input type="radio" name="compliment" value="awesome"> awesome
            <input type="radio" name="compliment" value="terrific"> terrific
            <input type="radio" name="compliment" value="fantastic"> fantastic
            <input type="radio" name="compliment" value="neato"> neato
            <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def diss_person():
  """Get user by name, then diss"""

  player = request.args.get("person")

  diss = choice(INSULTS)
      # compliment = choice(AWESOMENESS)

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think {}!
      </body>
    </html>
    """.format(player, diss)



if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
