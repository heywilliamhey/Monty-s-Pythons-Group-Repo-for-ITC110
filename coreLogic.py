# list o' classes

c14554 = {
	"name": "c14554",
	"prereq": []
}
classA = {
	"name": "classA",
	"prereq": [],
	"alt": c14554
}
classB = {
	"name": "classB",
	"prereq": [classA]
}

classC = {
	"name": "classC",
	"prereq": [classB]
}
classD = {
	"name": "classD",
	"prereq": [classC]
}
class1 = {
	"name": "class1",
	"prereq": []
}
c14553 = {
	"name": "c14553",
	"prereq": [classD, class1]
}
classE = {
	"name": "classE",
	"prereq": [classD, class1],
	"alt": c14553
}
Twopoint0 = {
	"name": "class2.0",
	"prereq": [class1]
}
class2 = {
	"name": "class2",
	"prereq": [class1],
	"alt": Twopoint0
}
class2plus1 = {
	"name": "class2+1",
	"prereq": [classA, class2]
}
class3 = {
	"name": "class3",
	"prereq": [classA, class2],
	"alt": class2plus1
}
class4 = {
	"name": "class4",
	"prereq": [class3]
}
class5 = {
	"name": "class5",
	"prereq": [class4]
}
classAZ = {
		'name': 'Class AZ',
		'units': 5,
		'prereq': [classA]
}
classZA = {
		'name': 'Class ZA',
		'units': 5,
		'prereq': [classA]
}
classVowel = {
		'name': 'Class Vowel',
		'units': 5,
		'prereq': [classA]
}
classConsonant = {
		'name': 'Class Consonant',
		'units': 10,
		'prereq': [classB]
}
classLowercase = {
		'name': 'Class Lowercase',
		'units': 5,
		'prereq': []
}
classCapital = {
		'name': 'Class Capital',
		'units': 5,
		'prereq': []
}
classPrime = {
		'name': 'Class Prime',
		'units': 10
}
classEven = {
		'name': 'Class Even',
		'units': 5

}
classOdd = {
		'name': 'Class Odd',
		'units': 5
}
classInfinity = {
		'name': 'Class Infinity',
		'units': 10
}
classAddSubtract = {
		'name': 'Class +-',
		'units': 5
}
classMultDivide = {
		'name': 'Class x/',
		'units': 10
}
# list o' electives
alphaElective = {
		'classList': [classAZ, classZA, classVowel, classConsonant, classLowercase, classCapital],
		'reqUnits': 20

}
numElect = {
		'classList': [classPrime, classEven, classOdd, classInfinity, classAddSubtract, classMultDivide],
		'reqUnits': 20
}
alphanumElect = {
		'classList': [classAZ, classZA, classVowel, classConsonant, classPrime, classEven, classOdd, classInfinity],
		'reqUnits': 15
}

# list o' majors
# IMPORTANT: Do not put a class before its prerequisites
alphanum = [classA, classB, classC, class1, class2, class3, alphanumElect]
alpha = [classA, class1, classB, classC, classD, classE, alphaElective]
numeric = [class1, classA, class2, class3, class4, class5, numElect]
majors = ["alpha", "numeric", "alphanum"]


def majorParse(m):  # takes input and turns it into variable
	return {
		"alpha": alpha,
		"numeric": numeric,
		"alphanum": alphanum
	}.get(m, None)

major = majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())  # set major.
while major is None:  # for invalid input
	print("I didn't understand that")
	major = majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())  # try again to set major. Forever.


def inParse(a):  # Takes user input and returns True/False/None
	i = ''.join(filter(str.isalpha, a))
	if i == "y":
		return True
	elif i == "n":
		return False
	else:
		print("I don't understand? Try y or n.")
		return None

currentClass = None  # The class we are looking at.
unReq = []  # Classes that have already been taken and are, therefore, no longer required
electiveUnits = 0
prospectiveElectives = []
candidateClasses = []  # Classes you can take


def prereqsMet(prereqs, taken):  # Looks at the classes you've taken and compares them to the prereqs of a class
	for i in prereqs:
		if i["name"] not in taken:  # if you haven't taken any of the prereqs you can not take the class
			return False
	return True


def promptTaken(courseName):
	taken = None
	while taken is None:
		taken = inParse(input("Have you taken %s? (y/n) " % courseName))
	return taken

for c in major:  # Looks through list of required classes
	if c.get('classList', None) is not None:
		for elective in c['classList']:
			if electiveUnits >= alphaElective['reqUnits']:
				break

			taken = promptTaken(elective['name'])
			if taken:
				electiveUnits += elective['units']
			else:
				prospectiveElectives.append(elective['name'])
		if electiveUnits < 20:
			candidateClasses += prospectiveElectives
		continue
	# exclude classes with prereqs you haven't taken
	if not prereqsMet(c["prereq"], unReq):
		continue

	taken = promptTaken(c["name"])
	if not taken:
		alternate = c.get("alt", None)  # Is there an alternate class?
		if alternate is not None:
			taken = promptTaken(alternate["name"])

	if taken:  # if you have taken a class or it's alternate it is no longer required.
		unReq.append(c["name"])
	else:
		# push remaining classes to candidate classes
		candidateClasses.append(c["name"])
		alternate = c.get("alt", None)
		if alternate is not None:  # If there is an alternate class you can take that too.
			candidateClasses.append(alternate["name"])
print("You can take", candidateClasses)
