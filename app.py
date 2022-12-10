from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from solve_ode import solve_ode

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

    # Use the number in the ODE
    fig, ax = solve_ode(number)
    # # Plot the number on a matplotlib plot
    # plt.plot([number])
    fig.show()
    # Save the plot to an image file
    fig.savefig("static/plot.png")

    # Render the plot on the webpage
    return render_template("plot.html")

if __name__ == "__main__":
    app.run()
