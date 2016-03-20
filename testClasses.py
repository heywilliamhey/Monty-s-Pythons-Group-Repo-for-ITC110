# list o' classes

c14554 = {
    'name': 'c14554',
    'credits': 5,
    'prereq': [],
    'offered': True
}
classA = {
    'name': 'classA',
    'credits': 5,
    'prereq': [],
    'alt': c14554,
    'offered': False
}
classB = {
    'name': 'classB',
    'credits': 5,
    'prereq': [classA],
    'offered': True
}

classC = {
    'name': 'classC',
    'credits': 5,
    'prereq': [classB],
    'offered': True
}
classD = {
    'name': 'classD',
    'credits': 5,
    'prereq': [classC],
    'offered': False
}
class1 = {
    'name': 'class1',
    'credits': 5,
    'prereq': [],
    'offered': True
}
c14553 = {
    'name': 'c14553',
    'credits': 5,
    'prereq': [classD, class1],
    'offered': False
}
classE = {
    'name': 'classE',
    'credits': 5,
    'prereq': [classD, class1],
    'alt': c14553,
    'offered': True
}
Twopoint0 = {
    'name': 'class2.0',
    'credits': 5,
    'prereq': [class1],
    'offered': True
}
class2 = {
    'name': 'class2',
    'credits': 5,
    'prereq': [class1],
    'alt': Twopoint0,
    'offered': False
}
class2plus1 = {
    'name': 'class2+1',
    'credits': 5,
    'prereq': [classA, class2],
    'offered': True
}
class3 = {
    'name': 'class3',
    'credits': 5,
    'prereq': [classA, class2],
    'alt': class2plus1,
    'offered': True
}
class4 = {
    'name': 'class4',
    'credits': 5,
    'prereq': [class3],
    'offered': False
}
class5 = {
    'name': 'class5',
    'credits': 5,
    'prereq': [class4],
    'offered': True
}
classAZ = {
        'name': 'Class AZ',
        'credits': 5,
        'prereq': [classA],
        'offered': True
}
classZA = {
        'name': 'Class ZA',
        'credits': 5,
        'prereq': [classA],
        'offered': True
}
classVowel = {
        'name': 'Class Vowel',
        'credits': 5,
        'prereq': [classA],
        'offered': False
}
classConsonant = {
        'name': 'Class Consonant',
        'credits': 10,
        'prereq': [classB],
        'offered': True
}
classLowercase = {
        'name': 'Class Lowercase',
        'credits': 5,
        'prereq': [],
        'offered': True
}
classCapital = {
        'name': 'Class Capital',
        'credits': 5,
        'prereq': [],
        'offered': False
}
classPrime = {
        'name': 'Class Prime',
        'credits': 10,
        'prereq': [class1],
        'offered': False
}
classEven = {
        'name': 'Class Even',
        'credits': 5,
        'prereq': [class2],
        'offered': True
}
classOdd = {
        'name': 'Class Odd',
        'credits': 5,
        'prereq': [class3],
        'offered': False
}
classInfinity = {
        'name': 'Class Infinity',
        'credits': 10,
        'prereq': [class5],
        'offered': False
}
classAddSubtract = {
        'name': 'Class +-',
        'credits': 5,
        'prereq': [],
        'offered': True
}
classMultDivide = {
        'name': 'Class x/',
        'credits': 10,
        'prereq': [],
        'offered': False
}
# list o' electives
alphaElective = {
        'name': 'alpha elective',
        'classList': [classAZ, classZA, classVowel, classConsonant, classLowercase, classCapital],
        'reqCredits': 20

}
numElect = {
        'name': 'numeric elective',
        'classList': [classPrime, classEven, classOdd, classInfinity, classAddSubtract, classMultDivide],
        'reqCredits': 20
}
alphanumElect = {
        'name': 'alphanumeric elective',
        'classList': [classAZ, classZA, classVowel, classConsonant, classPrime, classEven, classOdd, classInfinity],
        'reqCredits': 15
}

# list o' majors
# IMPORTANT: Do not put a class before its prerequisites
alphanum = [classA, classB, classC, class1, class2, class3, alphanumElect]
alpha = [classA, class1, classB, classC, classD, classE, alphaElective]
numeric = [class1, classA, class2, class3, class4, class5, numElect]


def majorParse(m):  # takes input and turns it into variable
    return {
        'alpha': alpha,
        'numeric': numeric,
        'alphanum': alphanum
    }.get(m, None)
