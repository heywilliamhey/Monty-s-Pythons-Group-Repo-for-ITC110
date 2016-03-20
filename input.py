def inParse(a):  # Takes user input and returns True/False/None
    i = ''.join(filter(str.isalpha, a))
    if i == "y":
        return True
    elif i == "n":
        return False
    else:
        print("I don't understand? Try y or n.")
        return None

def promptTaken(courseName):
    taken = None
    while taken is None:
        taken = inParse(input("Have you taken %s? (y/n) " % courseName))
    return taken