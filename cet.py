from flask import Flask, request, redirect, url_for, render_template
import pymysql

app = Flask(__name__)

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Amar@3142',
        database='cetform'
    )
    return connection

# Function to insert data into the MySQL database
def insert_data(mobile, name, score):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = '''INSERT INTO form_info (Mobile_Number, Student_name, Score)
                VALUES (%s, %s, %s);'''
        cursor.execute(query, (mobile,name,score))
        connection.commit()
        connection.close()
    except pymysql.connector.Error as err:
        print(f"Error: {err}")

@app.route('/', methods=['GET', 'POST'])
def index():
    rank = None
    if request.method == 'POST':
        mobile = request.form['mob']
        name = request.form['name1']
        score = float(request.form['score'])
        insert_data(mobile, name, score)
        # Insert data and calculate the rank based on the score
        rank  = int(180474 - ( score * 180474 / 100))+1


    return render_template('index.html', rank=rank)

@app.route('/thank-you')
def thank_you():
    return "Thank you for submitting your details!"

if __name__ == '__main__':
    app.run(debug=True)
