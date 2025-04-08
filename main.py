ogString = input("Enter the Equation (Write ^x for any subscript):")

# H(CO)^2 = H + C^2 + O^2
sides = ogString.split('=')
reactants = sides[0].split('+')
products = sides[1].split('+')

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

    print(f"sideSplit: {sideSplit}")

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

        print(f"Component: {comp}, Constant: {const}")

        if '(' in comp and ')' in comp:
            i = comp.index(')') + 2

            polyco = ''
            while i < len(comp) and comp[i].isdigit():
                polyco += comp[i]
                i += 1
            polyco = int(polyco)

            for x in range(actStart, len(comp)):
                if x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower():
                    i = x + 3
                    multiple = ''
                    while i < len(comp) and comp[i].isdigit():
                        multiple += comp[i]
                        i += 1
                    if multiple == '':
                        multiple = 1
                    else:
                        multiple = int(multiple)

                else:
                    i = x + 2
                    multiple = ''
                    while i < len(comp) and comp[i].isdigit():
                        multiple += comp[i]
                        i += 1
                    if multiple == '':
                        multiple = 1
                    else:
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
                        existing = sideVals[counter].get(f'{comp[x]}{comp[x + 1]}')
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + (const * polyco)})

                    # If 1 letter, in dictionary, and '^' doesn't follow
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] != '^':
                        existing = sideVals[counter].get(comp[x])
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
                        existing = sideVals[counter].get(f'{comp[x]}{comp[x + 1]}')
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + (const * polyco * multiple)})

                    # If 1 letter, in dictionary, and '^' follows
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] == '^':
                        existing = sideVals[counter].get(comp[x])
                        sideVals[counter].update({comp[x]: existing + (const * polyco * multiple)})
        else:
            print(f"Component 1: {comp}, Constant: {const}")
            for x in range(actStart, len(comp)):
                if x == len(comp) - 1:
                    if comp[x].isupper():
                        if comp[x] in sideVals[counter]:
                            sideVals[counter][comp[x]] += const
                        else:
                            sideVals[counter][comp[x]] = const
                    continue

                if x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower():
                    i = x + 3
                    multiple = ''
                    while i < len(comp) and comp[i].isdigit():
                        multiple += comp[i]
                        i += 1
                    if multiple == '':
                        multiple = 1
                    else:
                        multiple = int(multiple)

                else:
                    i = x + 2
                    multiple = ''
                    while i < len(comp) and comp[i].isdigit():
                        multiple += comp[i]
                        i += 1
                    if multiple == '':
                        multiple = 1
                    else:
                        multiple = int(multiple)

                    if len(comp) == 1:
                        sideVals[counter][comp[x]] = const

                    # If 2 letter, in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and f'{comp[x]}{comp[x+1]}' in sideVals[counter] and comp[x+2] != '^':
                        existing = int(sideVals[counter].get(f'{comp[x]}{comp[x+1]}'))
                        sideVals[counter].update({f'{comp[x]}{comp[x+1]}': existing + const})

                    # If 2 letter, not in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x+1].islower() and comp[x+2] != '^':
                        sideVals[counter][f'{comp[x]}{comp[x + 1]}'] = const

                    # If 1 letter, in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x] in sideVals[counter] and comp[x+1] != '^':
                        existing = int(sideVals[counter].get(comp[x]))
                        sideVals[counter].update({[comp[x]] : const + existing})

                    # If 1 letter, not in dictionary already, and there are no ^s
                    elif x < len(comp)-1 and comp[x].isupper() and comp[x+1] != '^':
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
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x] in sideVals[counter] and comp[x+1] == '^':
                        existing = int(sideVals[counter].get(comp[x]))
                        sideVals[counter].update({comp[x]: (const * multiple) + existing})

                    # If 1 letter, not in dictionary already, and there are ^s
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x+1] == '^':
                        sideVals[counter][comp[x]] = const * multiple
        counter += 1

    return sideVals
def mergeDicts(dicts):
    print('Merging...')
    result = dict()
    for i in dicts:
        for j in i:
            if j in result:
                result.update({j: i.get(j) + result.get(j)})
            else:
                result[j] = i.get(j)

    return result

def solveCheck(check1, check2):

    print('Checking')
    if check1 == check2:
        return True
    else:
        return False
def createEquation(reacts, prods):
    reactElements = mergeDicts(reacts)
    prodElements = mergeDicts(prods)
    elementList = list()
    elementList.append(reactElements)
    elementList.append(prodElements)
    elements = mergeDicts(elementList)

    for i in elements:
        for j in 


print(solveCheck(oneSide(reactants), oneSide(products)))

