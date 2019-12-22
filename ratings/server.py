"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Rating, Movie


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template('homepage.html')


@app.route('/users')
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Return a page showing the details of a given user."""

    user = User.query.filter_by(user_id=user_id).first()
    user_id = user.user_id
    email = user.email
    zipcode = user.zipcode
    age = user.age
    return render_template("user_details.html",
                           user_id=user_id,
                           email=email,
                           zipcode=zipcode,
                           age=age)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Return a page showing the details of a given movie.

    including a list of all the ratings.
    """
    movie = Movie.query.filter_by(movie_id=movie_id).first()
    movie_id = movie.movie_id
    title = movie.title
    released_at = movie.released_at
    imdb_url = movie.imdb_url
    ratings = movie.ratings
    return render_template("movie_details.html",
                           movie_id=movie_id,
                           title=title,
                           released_at=released_at,
                           imdb_url=imdb_url,
                           ratings=ratings)




@app.route('/register')
def register_user():
    """Show registration form.

    Get user email address and password.
    """

    return render_template("register.html")


@app.route('/handle_registration_form', methods=["POST"])
def handle_registration_form():
    """Handle registration form submission."""
    email = request.form.get("email")
    password = request.form.get("password")
    if User.query.filter_by(email=email).first():
        flash('Email address already taken. Please enter a different email.')
        return redirect("/register")
    else:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Successfully registered {email}.')
        return render_template("login.html")


@app.route('/login', methods=['GET'])
def login():
    """Shows login form."""
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def handle_login():
    email = request.form.get("email")
    password = request.form.get("password")
    login_user = User.query.filter_by(email=email).first()
    if login_user:
        if login_user.password == password:
            session['user_id'] = login_user.user_id
            flash(f'Logged in as {login_user.email}.')
            return redirect("/")
        else:
            flash('Incorrect password.')
            redirect('/login')
    else:
        flash('Invalid email.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('user_id')
    flash("You are logged out.")
    return redirect("/")


@app.route('/movies')
def movies():
    movies = Movie.query.order_by('title').all()
    return render_template('movies.html', movies=movies)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
