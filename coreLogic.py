#list o' classes
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
	"prereq":[classA]
}

classC = {
	"name": "classC",
	"prereq":[classB]
}
classD = {
	"name":"classD",
	"prereq":[classC]
}
class1 = {
	"name": "class1",
	"prereq": []
}
c14553 = {
	"name":"c14553",
	"prereq":[classD,class1]
}
classE = {
	"name":"classE",
	"prereq":[classD,class1],
	"alt":c14553
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
	"name":"class2+1",
	"prereq":[classA, class2]
}
class3 = {
	"name": "class3",
	"prereq": [classA, class2],
	"alt": class2plus1
}
class4 = {
	"name":"class4",
	"prereq": [class3]
}
class5 = {
	"name":"class5",
	"prereq":[class4]
}

#list o' majors
#IMPORTANT: Do not put a class before its prerequisites
alphanum = [classA, classB, classC , class1 , class2, class3]
alpha = [classA, class1, classB, classC, classD, classE]
numeric = [class1, classA, class2, class3, class4, class5]
majors = ["alpha","numeric","alphanum"]

def majorParse(major): #takes input and turns it into variable
	return {
		"alpha": alpha,
		"numeric": numeric,
		"alphanum": alphanum
	}.get(major,None)

major =  majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())#set major.
while major == None: #for invalid input
	print("I didn't understand that")
	major =  majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())#try again to set major. Forever.

def inParse(a): #Takes user input and returns True/False/None
	i = ''.join(filter(str.isalpha, a))
	if i == "y":
		return True
	elif i == "n":
		return False
	else:
		print("I don't understand? Try y or n.")
		return None

currentClass = None #The class we are looking at.
unReq = [] #Classes that have already been taken and are, therefore, no longer required
candidateClasses = [] #Classes you can take

def prereqsMet(prereqs,taken): #Looks at the classes you've taken and compares them to the prereqs of a class
	for i in prereqs:
		if i["name"] not in taken: #if you haven't taken any of the prereqs you can not take the class
			return False
	return True

def promptTaken(courseName):
	taken = None
	while taken is None:
		taken = inParse(input("Have you taken %s? (y/n) " % courseName))
	return taken

for i in major: #Looks through list of required classes
	currentClass = i
	#exclude classes with prereqs you haven't taken
	if not prereqsMet(i["prereq"],unReq):
		continue

	taken = promptTaken(currentClass["name"])
	if taken == False:
		alternate = currentClass.get("alt", None) #Is there an alternate class?
		if alternate != None:
			taken = promptTaken(alternate["name"])

	if taken == True: #if you have taken a class or it's alternate it is no longer required.
		unReq.append(currentClass["name"])
	else:
		#push remaining classes to candidate classes
		candidateClasses.append(i["name"])
		alternate = i.get("alt", None)
		if alternate != None: #If there is an alternate class you can take that too.
			candidateClasses.append(alternate["name"])
		continue
print(unReq)
print("You can take",candidateClasses)
