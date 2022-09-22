from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Weight, Macro, User, Food
from . import db
import json
from NutritionCalculator import UserMacros

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
	user = User.query.get_or_404(current_user.id)
	if request.method == 'POST':
		user.kcal = user.default_kcal
		user.carb = user.default_carb
		user.fat = user.default_fat 
		user.protein = user.default_protein
		db.session.add(user)
		db.session.commit()

	return render_template("home.html", user=current_user)


@views.route('/weight', methods=['GET', 'POST'])
@login_required
def weight():
	if request.method == 'POST':
		weight = request.form.get('weight')

		if len(weight) < 1:
			flash('Weight is too short!', category = 'error')
		else:
			new_weight = Weight(data=weight, user_id=current_user.id)
			db.session.add(new_weight)
			db.session.commit()
			flash('Weight added!', category = 'success')	

	return render_template("weight.html", user=current_user)


@views.route('/food', methods=['GET', 'POST'])
@login_required
def food():
	user = User.query.get_or_404(current_user.id)
	if request.method == 'POST':
		kcal = request.form.get('kcalConsumed')
		food_name = request.form.get('food_name')
		food_fat = request.form.get('food_fat')
		food_carb = request.form.get('food_carb')
		food_protein = request.form.get('food_protein')

		if len(kcal) < 1:
			flash('Calories too low!', category = 'error')
		else:
			new_food = Food(food_name=food_name, cal=kcal, food_fat=food_fat, food_carb=food_carb, food_protein=food_protein, user_id=current_user.id)
			user.kcal = user.kcal - int(kcal)
			user.carb = user.carb - int(food_carb)
			user.protein = user.protein - int(food_protein)
			user.fat = user.fat - int(food_fat)
			db.session.add(new_food)
			db.session.add(user)
			db.session.commit()
			flash('Food added!', category = 'success')
	return render_template("food.html", user=current_user)


@views.route('/exercise', methods=['GET', 'POST'])
@login_required
def exercise():
	return render_template("exercise.html", user=current_user)


@views.route('/program')
def program():
	return render_template("program.html", user=current_user)


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	user = User.query.get_or_404(current_user.id) # create the user object in order to use it. We declared User from models above.
	if request.method == 'POST':
		if request.form["gender_type"] == "MALE":
			sex = "M"
		elif request.form["gender_type"] == "FEMALE":
			sex = "F"
		weight = request.form.get('weight', type=float)
		height = request.form.get('height', type=float)
		age = request.form.get('age', type=int)
		if request.form["activity"] == "NOOB":
			activityFactor = 1
		elif request.form["activity"] == "BEGINNER":
			activityFactor = 2
		elif request.form["activity"] == "INTERMEDIATE":
			activityFactor = 3
		elif request.form["activity"] == "ADVANCED":
			activityFactor = 4
		elif request.form["activity"] == "ALL":
			activityFactor = 5		
		if request.form["diet_type"] == "BULK":
			diet = "B"
		elif request.form["diet_type"] == "CUT":
			diet = "C"
		countdown = request.form.get('countdown', type=int)

		if weight < 1:
			flash('Invalid weight.', category='error')
		elif height < 1:
			flash('Invalid height.', category='error')
		elif age < 1:
			flash('Invalid age.', category='error')
		else:
			user.sex = sex
			user.weight = weight
			user.height = height
			user.activityFactor = activityFactor
			user.diet = diet
			user.countdown = countdown

			nutritionProfile = UserMacros(sex, weight, height, age, activityFactor, diet)
			kcal = int(nutritionProfile.getCalories())
			carb = nutritionProfile.getMacroCarb()
			fat = nutritionProfile.getMacroFat()
			protein = nutritionProfile.getMacroProtein()

			user.default_kcal = kcal
			user.default_carb = carb
			user.default_fat = fat 
			user.default_protein = protein
			user.kcal = kcal
			user.carb = carb
			user.fat = fat 
			user.protein = protein
			db.session.add(user)
			db.session.commit()
			flash('Profile created!', category='success')

			return redirect(url_for('views.home'))
	return render_template("profile.html", user=current_user) 			


@views.route('/delete-weight', methods=['POST'])
def delete_weight():
    weight = json.loads(request.data)
    weightId = weight['weightId']
    weight = Weight.query.get(weightId)
    if weight:
        if weight.user_id == current_user.id:
            db.session.delete(weight)
            db.session.commit()

    return jsonify({})


@views.route('/delete-food', methods=['POST'])
def delete_food():
	user = User.query.get_or_404(current_user.id)
	food = json.loads(request.data)
	foodId = food['foodId']
	food = Food.query.get(foodId)
	if food:
		if food.user_id == current_user.id:
			user.kcal = user.kcal + food.cal
			user.carb = user.carb + food.food_carb
			user.protein = user.protein + food.food_protein
			user.fat = user.fat + food.food_fat
			db.session.delete(food)
			db.session.commit()
	return jsonify({})
