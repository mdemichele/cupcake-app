"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Cupcake, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True 
app.config['SECRET_KEY'] = 'anothersecretanotherseason'

debug = DebugToolbarExtension(app)

connect_db(app)

def serialize_cupcake(cupcake):
    """Helper function to serialize a cupcake SQLAlchemy obj to dictionary"""
    
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }
    
@app.route('/')
def get_home_page():
    """Returns the home page template"""
    return render_template("home.html")

@app.route('/api/cupcakes')
def get_all_cupcakes_data():
    """Returns ALL cupcake data"""
    # Get cupcakes from database 
    cupcakes = Cupcake.query.all()
    # Serialize the cupcakes 
    serialized_cupcakes = [serialize_cupcake(c) for c in cupcakes]
    # Return json object of cupcakes data 
    return jsonify(cupcakes=serialized_cupcakes)
    
@app.route('/api/cupcakes/<cupcakeId>')
def get_one_cupcake_data(cupcakeId):
    """Returns data for specified cupcake"""
    # Get cupcake data from database 
    cupcake = Cupcake.query.get_or_404(cupcakeId)
    
    serialized = serialize_cupcake(cupcake)
    
    return jsonify(cupcake=serialized)
    
@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Creates a new cupcake"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]
    
    newCupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    
    db.session.add(newCupcake)
    db.session.commit()
    
    serialized_cupcake = serialize_cupcake(newCupcake)
    
    data = jsonify(cupcake=serialized_cupcake)
    
    return data, 201
    
@app.route('/api/cupcakes/<cupcakeId>', methods=["PATCH"])
def update_cupcake(cupcakeId):
    """Updates the specified cupcake"""
    # Get data from request 
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]
    
    # Get object from database 
    cupcake = Cupcake.query.get_or_404(cupcakeId)
    
    # Update cupcake object and save to database 
    cupcake.flavor = flavor 
    cupcake.size = size 
    cupcake.rating = rating 
    cupcake.image = image 
    
    db.session.add(cupcake)
    db.session.commit()
    
    serialized_data = serialize_cupcake(cupcake)
    
    jsonData = jsonify(cupcake=serialized_data)
    return jsonData, 200
    
@app.route('/api/cupcakes/<cupcakeId>', methods=["DELETE"])
def delete_cupcake(cupcakeId):
    """Deletes the specified cupcake"""
    # Attempt to delete the cupcake 
    check_if_cupcake_exists = Cupcake.query.get_or_404(cupcakeId)
    cupcake = Cupcake.query.filter_by(id=cupcakeId).delete()
    
    return jsonify({"message": "Deleted"})
    
    
    
    
    
    
    
    
    
    
    
    
    
    