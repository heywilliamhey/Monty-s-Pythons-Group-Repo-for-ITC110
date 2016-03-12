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
        'units': 10,
        'prereq': [class1]
}
classEven = {
        'name': 'Class Even',
        'units': 5,
        'prereq': [class2]

}
classOdd = {
        'name': 'Class Odd',
        'units': 5,
        'prereq': [class3]
}
classInfinity = {
        'name': 'Class Infinity',
        'units': 10,
        'prereq': [class5]
}
classAddSubtract = {
        'name': 'Class +-',
        'units': 5,
        'prereq': []
}
classMultDivide = {
        'name': 'Class x/',
        'units': 10,
        'prereq': []
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