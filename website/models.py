from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): # Notes blueprint (every note will look like this)
	id = db.Column(db.Integer, primary_key = True) # each note will have a unique ID
	data = db.Column(db.String(10000)) # Note will have a max string of 10000 characters
	date = db.Column(db.DateTime(timezone = True), default =func.now()) # allow Notes to generate the current date 
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # associate different info with different users


class Food(db.Model): 
	id = db.Column(db.Integer, primary_key = True) 
	cal = db.Column(db.Integer) # Food calories
	date = db.Column(db.DateTime(timezone = True), default =func.now()) # allow Diary to generate the current date
	food_name = db.Column(db.String(10000)) # Food will have a max string of 10000 characters
	food_fat = db.Column(db.Integer)
	food_carb = db.Column(db.Integer)
	food_protein = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # associate different info with different users


class Weight(db.Model): # Weight blueprint (every weight will look like this)
	id = db.Column(db.Integer, primary_key = True) # each weight will have a unique ID
	data = db.Column(db.String(10000))
	date = db.Column(db.DateTime(timezone = True), default =func.now()) # allow Weights to generate the current date 
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # associate different info with different users


class Macro(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	fat = db.Column(db.Integer)
	carb = db.Column(db.Integer)
	protein = db.Column(db.Integer)
	kcal = db.Column(db.Float)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin): # Users blueprint (every user will have these attributes)
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(150), unique = True)
	password = db.Column(db.String(150))
	first_name = db.Column(db.String(150))
	sex = db.Column(db.String(1))
	weight = db.Column(db.Float)
	height = db.Column(db.Float)
	age = db.Column(db.Integer)
	activityFactor = db.Column(db.Integer)
	countdown = db.Column(db.Integer)
	diet = db.Column(db.String(1))
	default_fat = db.Column(db.Integer)
	default_carb = db.Column(db.Integer)
	default_protein = db.Column(db.Integer)
	default_kcal = db.Column(db.Integer)
	fat = db.Column(db.Integer)
	carb = db.Column(db.Integer)
	protein = db.Column(db.Integer)
	kcal = db.Column(db.Integer)
	notes = db.relationship('Note') # stores all of the different notes for this particular user	
	weights = db.relationship('Weight')
	macros = db.relationship('Macro')
	foods = db.relationship('Food')

