from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<restaurant>")
def index(restaurant=None):
    return render_template('restaurant.html', restaurant=restaurant)


@app.route("/list")
def list():
    with open ('restaurants.txt', 'r') as f:
        content = f.read()
    return render_template("list.html", content=content)



if __name__ == "__main__":
    app.run()

