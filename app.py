from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# ✅ MongoDB Atlas connection (apna username/password replace karo)
client = MongoClient("mongodb+srv://vivekbhagwat29_db_user:KOjyBjEerYgOg51A@cluster0.du1pssz.mongodb.net/assignmentdb?retryWrites=true&w=majority&appName=Cluster0")

db = client.assignmentdb
collection = db.students

# ✅ API route (data.json se data return karega)
@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Form page
@app.route('/')
def form():
    return render_template("form.html")

# ✅ Form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        age = request.form['age']

        # MongoDB insert
        collection.insert_one({"name": name, "age": int(age)})

        return render_template("success.html")
    except Exception as e:
        return render_template("form.html", error=str(e))

if __name__ == '__main__':
    app.run(debug=True)


