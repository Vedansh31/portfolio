from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Connection to HomePage
@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<page_name>")
def any_page(page_name):
    return render_template(page_name)

# Taking Data from the User
@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/tq.html')
    else:
        return 'Try Again!!'