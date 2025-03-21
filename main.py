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

    counter = 0
    for comp in sideSplit:
        skipNext = False
        poly = False

        coStr = ''

        i = 0
        while i < len(comp) and comp[i].isdigit():
            coStr += comp[i]
            i += 1
        const = int(coStr)
        actStart = i
        sideConsts.append(const)


        if '(' in comp and ')' in comp:
            poly = True
            i = comp.index('(')

            polyco = ''
            while i < len(comp) and comp[i].isdigit():
                polyco += comp[i]
                i += 1
            polyco = int(polyco)
            for x in range(actStart, len(comp)-1):

                if x > comp.index(')') or x < comp.index('('):

                    # If 2 letter, in dictionary already, and there are no ^s
                    if x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and f'{comp[x]}{comp[x+1]}' in sideVals[counter] and '^' not in comp:
                        existing = int(sideVals[counter].get(f'{comp[x]}{comp[x+1]}'))
                        sideVals[counter].update({f'{comp[x]}{comp[x+1]}': existing + const})

                    # If 2 letter, not in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and '^' not in comp:
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': const})

                    # If 1 letter, in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x] in sideVals[counter] and '^' not in comp:
                        existing = int(sideVals[counter].get(comp[x]))
                        sideVals[counter].update({comp[x]: const + existing})

                    # If 1 letter, not in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and '^' not in comp:
                        sideVals[counter].update({comp[x]: const})

                    # Start of ^s

                    # If 2 letter, in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and f'{comp[x]}{comp[x + 1]}' in sideVals[counter]:
                        existing = int(sideVals[counter].get(f'{comp[x]}{comp[x + 1]}'))
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + const})

                    # If 2 letter, not in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower():
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': const})

                    # If 1 letter, in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] in sideVals[counter]:
                        existing = int(sideVals[counter].get(comp[x]))
                        sideVals[counter].update({comp[x]: const + existing})

                    # If 1 letter, not in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper():
                        sideVals[counter].update({comp[x]: const})
