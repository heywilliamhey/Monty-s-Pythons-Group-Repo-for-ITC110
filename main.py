from testClasses import *
from coreLogic import *
from input import *

while True:
    major = majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())  # set major.
    while major is None:  # for invalid input
        print("I didn't understand that")
        major = majorParse(input("What is your major? (alpha/numeric/alphanum) ").lower())  # try again to set major.

    unReq = []  # Classes that have already been taken and are, therefore, no longer required
    candidateClasses = []  # Classes you can take

    for c in major:  # Looks through list of required classes

        if c.get('classList', None) is not None:
            candidateClasses += handleElect(c, unReq)
            continue

        if not prereqsMet(c['prereq'], unReq):
                continue
        taken = promptTaken(c['name'])
        if not taken:
            alternate = c.get('alt', None)  # Is there an alternate class?
            if alternate is not None:
                taken = promptTaken(alternate['name'])

        if taken:  # if you have taken a class or it's alternate it is no longer required.
            unReq.append(c['name'])
        else:
            # push remaining classes to candidate classes
            candidateClasses.append(c['name'])
            alternate = c.get('alt', None)
            if alternate is not None:  # If there is an alternate class you can take that too.
                candidateClasses.append(alternate['name'])
    print("You can take", candidateClasses)
