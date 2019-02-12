from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",number_of_rows=8, number_of_columns=8, color1="red", color2="black")

@app.route("/<rows>")
def display_rows(rows):
    return render_template("index.html",number_of_rows=int(rows), number_of_columns=8, color1="red", color2="black")

@app.route("/<rows>/<cols>")
def display_rows_and_columns(rows, cols):
    return render_template("index.html",number_of_rows=int(rows), number_of_columns=int(cols), color2="black", color1="red")

@app.route("/<rows>/<cols>/<color1>/<color2>")
def display_colors(rows, cols, color1, color2):
    return render_template("index.html",number_of_rows=int(rows), number_of_columns=int(cols), color2=color2, color1=color1)





if __name__ == "__main__":
    app.run(debug=True)