from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/o-meni")
def about():
    return render_template("about.html")

# met kocke... random (1-6)
@app.route("/kocka")
def dice():
    return render_template("dice.html", kocka = random.randint(1,6))



# met kocke... random (1-N)
@app.route("/kocka/<N>")
def dice2(N):
    rnd=random.randint(1,int(N))
    print(rnd)
    return render_template("dice.html", kocka = rnd)



app.run(debug = True)


