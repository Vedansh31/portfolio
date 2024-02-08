from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Connection to HomePage
@app.route("/")
def my_home():
    return render_template('index.html')
# Dynamic Routing
@app.route("/<page_name>")
def any_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as my_db:
#         name = data['name']
#         e_mail = data['email']
#         msg = data['message']
#         file = my_db.write(f"\nname = {name} \ne-mail = {e_mail} \nmessage = {msg}")

# Writing to a csv file
def write_to_csv(data):
    with open('database.csv', newline= '', mode= 'a') as my_db:
        name = data['name']
        e_mail = data['email']
        msg = data['message']
        file_csv = csv.writer(my_db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)  
        file_csv.writerow([name, e_mail, msg])

# Taking Data from the User
@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/tq.html')
    else:
        return 'Something went wrong, Try Again!'