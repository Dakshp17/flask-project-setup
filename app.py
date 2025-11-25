from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# ----------------------------
# MongoDB Atlas Connection
# ----------------------------
client = MongoClient("mongodb+srv://dakshpatel:Daksh2004@cluster0.aqgsg24.mongodb.net/?appName=Cluster0")
db = client['studentDB']         # Database name
collection = db['students']      # Collection name

# ----------------------------
# Route: Show Form
# ----------------------------
@app.route('/')
def form():
    return render_template('form.html')

# ----------------------------
# Route: Handle Form Submission
# ----------------------------
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the HTML form
    name = request.form['name']
    course = request.form['course']

    # Insert data into MongoDB
    collection.insert_one({
        "name": name,
        "course": course
    })

    # Redirect to success page
    return redirect(url_for('success'))

# ----------------------------
# Route: Success Page
# ----------------------------
@app.route('/success')
def success():
    return render_template('success.html')

# ----------------------------
# Run the App
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)
