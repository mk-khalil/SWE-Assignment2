from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'test' and password == 'test':
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)