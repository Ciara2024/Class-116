from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message" : "It's a good day:)"
    })

@app.route("/Intro")
def new_api():
    return jsonify({
        "message" : "Hello there!"
    })

@app.route("/Text")
def about_me():
    my_name = "Ciara Alexander"
    return render_template("index.html", title="Introduction about Me", name = my_name)

@app.route("/form", methods=['GET','POST'])
def new_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return "Hello, {}!! \nYour email is {}".format(name,email)
    return render_template("intro.html")

if __name__ == '__main__':
    app.run()