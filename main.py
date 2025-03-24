ogString = input("Enter the Equation (Write ^x for any subscript):")

# H(CO)^2 = H + C^2 + O^2
sides = ogString.split('=')
reactants = ogString[0].split('+')

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
        if coStr != '':
            const = int(coStr)
        else:
            const = 1
        actStart = i
        sideConsts.append(const)


        if '(' in comp and ')' in comp:
            poly = True
            i = comp.index(')') + 2

            polyco = ''
            while i > len(comp) and comp[i].isdigit():
                polyco += comp[i]
                i += 1
            polyco = int(polyco)
            for x in range(actStart, len(comp)-1):
                if x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower():
                    i = x + 3
                    multiple = ''
                    while i > len(comp) and comp[i].isdigit():
                        multiple += comp[i]
                        i += 1
                    multiple = int(multiple)

                else:
                    i = x + 2
                    multiple = ''
                    while i > len(comp) and comp[i].isdigit():
                        multiple += comp[i]
                        i += 1
                    multiple = int(multiple)

                if x > comp.index(')') or x < comp.index('('):

                    # If 2 letter, in dictionary already, and there are no ^s
                    if x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and f'{comp[x]}{comp[x+1]}' in sideVals[counter] and comp[x+2] != '^':
                        existing = int(sideVals[counter].get(f'{comp[x]}{comp[x+1]}'))
                        sideVals[counter].update({f'{comp[x]}{comp[x+1]}': existing + const})

                    # If 2 letter, not in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and comp[x+2] != '^':
                        sideVals[counter][f'{comp[x]}{comp[x + 1]}'] = const

                    # If 1 letter, in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x] in sideVals[counter] and comp[x+2] != '^':
                        existing = int(sideVals[counter].get(comp[x]))
                        sideVals[counter].update({[comp[x]] : const + existing})

                    # If 1 letter, not in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x+2] != '^':
                        sideVals[counter][comp[x]] = const

                    # Start of ^s

                    # If 2 letter, in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and f'{comp[x]}{comp[x + 1]}' in sideVals[counter] and comp[x+2] == '^':
                        existing = int(sideVals[counter].get(f'{comp[x]}{comp[x + 1]}'))
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + (const * multiple)})

                    # If 2 letter, not in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and comp[x+2] == '^':
                        sideVals[counter][comp[x]+comp[x + 1]] = const * multiple

                    # If 1 letter, in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] in sideVals[counter] and comp[x+2] == '^':
                        existing = int(sideVals[counter].get(comp[x]))
                        sideVals[counter].update({comp[x]: (const * multiple) + existing})

                    # If 1 letter, not in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x+2] == '^':
                        sideVals[counter][comp[x]] = const * multiple

                elif x > comp.index('(') and x < comp.index(')'):

                    # If 2 letter, not in dictionary, and '^' doesn't follow
                    if x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and comp[x + 2] and f'{comp[x]}{comp[x+1]}' not in sideVals[counter] and comp[x+3] != '^':
                        sideVals[counter][f'{comp[x]}{comp[x+1]}'] = const * polyco

                    # If 1 letter, not in dictionary, and '^' doesn't follow
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x+2] != '^':
                        sideVals[counter][comp[x]] = const * polyco

                    # If 2 letter, in dictionary, and '^' doesn't follow
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and comp[
                        x + 2] and f'{comp[x]}{comp[x + 1]}' not in sideVals[counter] and comp[x + 3] != '^':
                        existing = sideVals.get(f'{comp[x]}{comp[x + 1]}')
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + (const * polyco)})

                    # If 1 letter, in dictionary, and '^' doesn't follow
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] != '^':
                        existing = sideVals.get(comp[x])
                        sideVals[counter].update({comp[x]: existing + (const * polyco)})

                    # '^' follows

                    # If 2 letter, not in dictionary, and '^' follows
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and comp[x + 2] and f'{comp[x]}{comp[x + 1]}' not in sideVals[counter] and comp[x + 3] == '^':
                        sideVals[counter][f'{comp[x]}{comp[x + 1]}'] = const * polyco * multiple

                    # If 1 letter, not in dictionary, and '^' follows
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] == '^':
                        sideVals[counter][comp[x]] = const * polyco * multiple

                    # If 2 letter, in dictionary, and '^' follows
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and comp[x + 2] and f'{comp[x]}{comp[x + 1]}' not in sideVals[counter] and comp[x + 3] == '^':
                        existing = sideVals.get(f'{comp[x]}{comp[x + 1]}')
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + (const * polyco * multiple)})

                    # If 1 letter, in dictionary, and '^' follows
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] == '^':
                        existing = sideVals.get(comp[x])
                        sideVals[counter].update({comp[x]: existing + (const * polyco * multiple)})

    return sideVals

print(oneSide(reactants))
