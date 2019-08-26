from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "ahmad"
    letter = list(name)
    return render_template("basic.html",
                            name=name,
                            letter=letter)
@app.route('/demo')
def demo_page():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
