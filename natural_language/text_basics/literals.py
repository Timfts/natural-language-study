# f string literals
def string_literals(useBeforeP3: bool = False):
    firstName = "italo"
    secondName = "Fontes"

    beforeP3 = "my name is {firstName} {secondName} (P2)".format(
        firstName=firstName, secondName=secondName)

    afterP3 = f"my name is {firstName} {secondName} (P3)"

    if useBeforeP3:
        print(beforeP3)
    else:
        print(afterP3)