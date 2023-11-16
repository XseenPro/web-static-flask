from flask import Flask, render_template, request, url_for, session, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

# @app.route('/tampilan_user')
# def tmpuser():
#     return render_template('index.html', active_page='index')

@app.route('/mobil')
def mobil():
    return render_template('mobil.html', active_page='mobil')

@app.route('/booking')
def booking():
    return render_template('booking_user.html', active_page='booking')

@app.route('/login')
def login():
    return render_template('login.html', active_page='login')

if __name__ == '__main__':
    app.run()
