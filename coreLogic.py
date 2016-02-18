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
class1 = {
	"name": "class1",
	"prereq": []
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
class3 = {
	"name": "class3",
	"prereq": [classA, class2]
}
alphanum = [classA, classB, classC , class1 , class2, class3]
#set major
major = alphanum
def inParse(a):
	i = ''.join(filter(str.isalpha, a))
	if i == "y":
		return True
	elif i == "n":
		return False
	else:
		print("I don't understand? Try y or n.")
		return None
currentClass = None
unReq = []
candidateClasses = []
def prereqsMet(prereqs,taken):
	for i in prereqs:
		if i["name"] not in taken:
			return False
	return True
for i in major:
	currentClass = i
	taken = inParse(input("Have you taken "+currentClass["name"]+"? y/n"))
	while taken == None:
		taken = inParse(input("Have you taken "+currentClass+"? y/n"))
	if taken == True:
		unReq.append(currentClass["name"])
	else:
		continue
print(unReq)
for i in major:
	#exclude classes already taken
	if i["name"] in unReq:
		continue
	#exclude classes with required classes not in unReq
	if not prereqsMet(i["prereq"],unReq):
		continue
	#push remaining classes to candidate classes
	candidateClasses.append(i["name"])
print("You can take",candidateClasses)
