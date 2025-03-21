ogString = input("Enter the Equation (Write ^x for any subscript):")

# H(CO)^2 = H + C^2 + O^2

def oneSide(side):
    sideSplit = []
    sideConsts = []
    sideDict = dict()
    polyDict = dict()
    sideVals = []
    for i in range(len(side)):
        # Remove spaces first, then convert to list
        sideSplit.append(list(side[i].replace(" ", "")))
        sideVals.append(dict())

    for comp in sideSplit:
        skipNext = False
        poly = False

        if '(' in comp and ')' in comp:
            poly = True
            i = comp.index('(')

            polyco = ''
            while i < len(comp) and comp[i].isdigit():
                polyco += comp[i]
                i += 1
            polyco = int(polyco)
            for

        coStr = ''

        i = 0
        while i < len(comp) and comp[i].isdigit():
            coStr += comp[i]
            i += 1
        const = int(coStr)
        sideConsts.append(const)

