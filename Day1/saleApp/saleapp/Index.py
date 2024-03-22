from flask import render_template

from Day1.saleApp.saleapp import app
from Day1.saleApp.saleapp import dao

@app.route("/")
def index():
    categories = dao.load_categories()
    return render_template("index.css", categories = categories)


if __name__ == '__main__':
    app.run(debug=True)
