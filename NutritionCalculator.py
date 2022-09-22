class UserMacros():
	userCount = 0

	def __init__(self, sex, weight, height, age, activityFactor, diet):

		self.sex = sex
		self.weight = float(weight) * 0.453592 # lbs to kg
		self.height = float(height) * 2.54  # in to cm
		self.age = age
		self.activityFactor = int(activityFactor)
		self.diet = diet

	def getRMR(self):
		if self.sex == "M":
			return (10*self.weight) + (6.25*self.height) - (5*self.age) + 5
		else:
		 	return (10*self.weight) + (6.25*self.height) - (5*self.age) - 161

	def baseCalories(self):
		if self.activityFactor == 1:
			return 1.2 * self.getRMR()
		elif self.activityFactor == 2:
			return 1.375 * self.getRMR()
		elif self.activityFactor == 3:
			return 1.55 * self.getRMR()
		elif self.activityFactor == 4:
			return 1.725 * self.getRMR()
		elif self.activityFactor == 5:
			return 1.9 * self.getRMR()

	def getCalories(self):
		if self.diet == "C":
			return self.baseCalories() * 0.80
		elif self.diet == "B":
			return self.baseCalories() * 1.20

	def getMacroCarb(self):
		return (self.getCalories() * 0.30) // 4.0

	def getMacroFat(self):
		return (self.getCalories() * 0.30) // 9.0

	def getMacroProtein(self):
		return (self.getCalories() * 0.40) // 4.0