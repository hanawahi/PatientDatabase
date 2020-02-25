from flask import Flask, render_template, request
import sqlite3 as sql
# Author: Hana Wahi
# Email: HQW5245@psu.edu
# See README for further details.

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


# Main/Index app route:
@app.route('/')
def index():
    return render_template('index.html')


# App route for navigating to "add" or "delete" web pages:
@app.route('/select', methods=['POST'])
def select():
    selected = request.form.get('selection')
    connection = sql.connect('database.db')
    connection.execute(
        # For each value inserted into the database, a new and unique
        # PID is assigned to the value using SqLite's autoincrement feature.
        # If the table does not exist, one is created.
        'CREATE TABLE IF NOT EXISTS users(PID INTEGER primary key autoincrement, firstname TEXT, lastname TEXT);')
    cursor = connection.execute('SELECT * FROM users;')
    result = cursor.fetchall()
    if selected == 'Add':
        if result:
            return render_template('input.html', result=result)
        return render_template('input.html')
    if selected == 'Delete':
        if result:
            return render_template('delete.html', result=result)
        return render_template('delete.html')
    else:
        return render_template('index.html')


# App route for adding/inserting entries:
@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('input.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('input.html', error=error)


# App route for removing/deleting entries:
@app.route('/delete', methods=['POST', 'GET'])
def delete():
    error = None
    if request.method == 'POST':
        result = valid_name_delete(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('delete.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('delete.html', error=error)


# Function for SQL commands (inserting)
def valid_name(first_name, last_name):
    connection = sql.connect('database.db')
    # For each value inserted into the database, a new and unique
    # PID is assigned to the value using SqLite's autoincrement feature.
    # If the table does not exist, one is created.
    connection.execute('CREATE TABLE IF NOT EXISTS users(PID INTEGER primary key autoincrement, firstname TEXT, lastname TEXT);')
    connection.execute('INSERT INTO users (firstname, lastname) VALUES (?,?);', (first_name, last_name))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


# Function for SQL commands (deleting)
def valid_name_delete(first_name, last_name):
    query = "DELETE FROM users WHERE firstname = ? AND lastname = ?"
    connection = sql.connect('database.db')
    # For each value inserted into the database, a new and unique
    # PID is assigned to the value using SqLite's autoincrement feature.
    # If the table does not exist, one is created first.
    connection.execute('CREATE TABLE IF NOT EXISTS users(PID INTEGER primary key autoincrement, firstname TEXT, lastname TEXT);')
    connection.execute(query, (first_name, last_name))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


if __name__ == "__main__":
    app.run()


