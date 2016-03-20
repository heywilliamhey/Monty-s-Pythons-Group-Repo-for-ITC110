from input import *


def prereqsMet(prereqs, taken):  # Looks at the classes you've taken and compares them to the prereqs of a class
    for i in prereqs:
        if i['name'] not in taken:  # if you haven't taken any of the prereqs you can not take the class
            return False
    return True


def handleElect(electives, newUnreq, reqCredits):
        # elective handling
        electiveCredits = 0
        prospectiveElectives = []
        for elective in electives:
            if electiveCredits >= reqCredits:
                break
            # testing prereqs: Can I move this out?
            if not prereqsMet(elective['prereq'], newUnreq):
                continue
            # Have they taken it?: Can I move this out?
            taken = promptTaken(elective['name'])
            alternate = elective.get('alt', None)  # Is there an alternate class?
            if not taken:
                if alternate is not None:
                    taken = promptTaken(alternate['name'])
            if taken:
                newUnreq.append(elective['name'])
                electiveCredits += elective['credits']
            else:
                prospectiveElectives.append(elective['name'])
                if alternate is not None:
                    prospectiveElectives.append(alternate['name'])
        # more elective handling
        if electiveCredits < reqCredits:
            return prospectiveElectives
        # exclude classes with prereqs you haven't taken

