from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/MarsDB_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
 
    #Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", marsinfo=mars_data)

    # R eturn template and data


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # =scrape_marsmongo.db.mars
    # Run the scrape function
    MarsData= scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    #mongo.db.collection.update({}, mars_data, upsert=True)
    mongo.db.collection.update({},MarsData, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
