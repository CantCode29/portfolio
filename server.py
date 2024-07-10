from flask import Flask, render_template, url_for, request, redirect
import csv
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, 'database.csv')

        with open(file_path, mode='a',newline='') as database:
            first_name = data.get('name')
            email = data.get("email")
            phone_number = data.get("phone")
            message = data.get("message")
            csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([first_name, email, phone_number, message])
    except Exception as e:
        print(f'something went wrong lol heres the error {e}')



@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('/ThankYou.html#section-contact')
    else:
        return "form not submitted"
