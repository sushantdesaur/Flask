
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home() -> "html":
    title = "Flask Home"
    return render_template("main_app/home.html",
                            the_title = title,)

@app.route("/products")
def products() -> "str":
    return "This is the products page"

@app.route("/help")
def help() -> "html":
    title = "Flask Help"
    return render_template("main_app/help.html",
                            the_title = title,)

@app.route("/about")
def about() -> "html":
    title = "About us"
    return render_template("main_app/about.html",
                            the_title = title,)


@app.route("/blog")
def blog() -> "html":
    title = "Flask Blog"
    return render_template("blog_app/blog.html",
                            the_title = title,)


if __name__ == "__main__":
    app.run(debug=True, port=9000)

