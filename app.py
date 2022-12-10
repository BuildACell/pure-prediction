from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates/index.html")

@app.route("/plot", methods=["POST"])
def plot():
    # Get the string input from the user
    string = request.form["string"]

    # Convert the string to a number
    number = int(string)

    # Plot the number on a matplotlib plot
    plt.plot([number])

    # Save the plot to an image file
    plt.savefig("static/plot.png")

    # Render the plot on the webpage
    return render_template("plot.html")

if __name__ == "__main__":
    app.run()
