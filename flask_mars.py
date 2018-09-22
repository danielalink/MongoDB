from flask import Flask, render_template, redirect
from pymongo import MongoClient
from scrape_mars import scrape

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client.Mars
collection = db.scrape_mars


@app.route("/")
def home():
    return render_template("index.html", mars=collection.find_one())

@app.route("/scrape", methods=['GET', 'POST'])
def reload():
    collection.update({"_id": 1}, {"$set": scrape()}, upsert = True)
    return redirect("http://localhost:5000/", code=302)
    

if __name__ == '__main__':
    app.run(debug=True)
