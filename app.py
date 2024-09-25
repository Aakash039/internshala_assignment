from flask import Flask, render_template

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "It always seems impossible until it's done. - Nelson Mandela",
    # Add more quotes here
]

@app.route("/")
def index():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run()