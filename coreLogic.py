from input import *


def prereqsMet(prereqs, taken):  # Looks at the classes you've taken and compares them to the prereqs of a class
    for i in prereqs:
        if i['name'] not in taken:  # if you haven't taken any of the prereqs you can not take the class
            return False
    return True


def handleElect(electives, newUnreq):
        electiveCredits = 0
        prospectiveElectives = []
        for elective in electives['classList']:
            if electiveCredits >= electives['reqCredits']:
                break

            if not prereqsMet(elective['prereq'], newUnreq):
                continue
            taken = promptTaken(elective['name'])
            if taken:
                newUnreq.append(elective['name'])
                electiveCredits += elective['credits']
            else:
                prospectiveElectives.append(elective['name'])
        if electiveCredits < 20:
            return prospectiveElectives
        # exclude classes with prereqs you haven't taken

