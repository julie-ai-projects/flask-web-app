from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    idea = None
    if request.method == "POST":
        topic = request.form.get("topic")
        idea = f"💡 Here's an idea for your topic '{topic}': Build a Python-based automation tool!"
    return render_template("index.html", idea=idea)

if __name__ == "__main__":
    app.run(debug=True)
