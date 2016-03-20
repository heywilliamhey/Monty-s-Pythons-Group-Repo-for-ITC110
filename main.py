from testClasses import *
from coreLogic import *
from input import *

while True:
    major = majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())  # set major.
    while major is None:  # for invalid input
        print("I didn't understand that")
        major = majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())  # try again to set major.

    taken = []  # Classes that have already been taken and are, therefore, no longer required
    unTaken = []
    candidateClasses = []  # Classes you can take

    for c in major:  # Looks through list of required classes

        if c.get('classList', None) is not None:
            candidateClasses.extend(handleElect(c['classList'], taken, c['reqCredits']))
            continue

        extension = handleElect([c], taken, c['credits'])
        if extension is not None:
            candidateClasses.extend(extension)
    print("You can take", candidateClasses)
