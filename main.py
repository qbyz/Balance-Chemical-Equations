from sympy import Matrix, lcm

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

        #print(f"Component: {comp}, Constant: {const}")

        if '(' in comp and ')' in comp:
            i = comp.index(')') + 2

            polyco = ''
            while i < len(comp) and comp[i].isdigit():
                polyco += comp[i]
                i += 1
            if polyco == '':
                polyco = 1
            else:
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
                        sideVals[counter].update({comp[x] : const + existing})

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
                    elif x < len(comp)-2 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x+2] != '^':
                        sideVals[counter][comp[x]] = const * polyco

                    # If 2 letter, in dictionary, and '^' doesn't follow
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and comp[
                        x + 2] and f'{comp[x]}{comp[x + 1]}' not in sideVals[counter] and comp[x + 3] != '^':
                        existing = sideVals[counter].get(f'{comp[x]}{comp[x + 1]}')
                        sideVals[counter].update({f'{comp[x]}{comp[x + 1]}': existing + (const * polyco)})

                    # If 1 letter, in dictionary, and '^' doesn't follow
                    elif x < len(comp) - 2 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] != '^':
                        existing = sideVals[counter].get(comp[x])
                        sideVals[counter].update({comp[x]: existing + (const * polyco)})

                    # '^' follows

                    # If 2 letter, not in dictionary, and '^' follows
                    elif x < len(comp) - 1 and comp[x].isupper() and comp[x + 1].islower() and comp[x + 2] and f'{comp[x]}{comp[x + 1]}' not in sideVals[counter] and comp[x + 3] == '^':
                        sideVals[counter][f'{comp[x]}{comp[x + 1]}'] = const * polyco * multiple

                    # If 1 letter, not in dictionary, and '^' follows
                    elif x < len(comp) - 2 and comp[x].isupper() and comp[x] not in sideVals[counter] and comp[x + 2] == '^':
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
                    print(f'HI {multiple}')

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
                print(f'MULTIPLE {multiple}')
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
                    sideVals[counter].update({comp[x] : const + existing})

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
    print(f'Dictionary: {sideVals}')
    return sideVals
def mergeDicts(dicts):
    #print('Merging...')
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
    elementList = reacts + prods
    elements = mergeDicts(list(reactElements) + list(prodElements))
    totals = list(mergeDicts(prods)) + list(mergeDicts(prods))
    vectList = [[] for i in range(len(elementList))]
    for i in elementList:
        for j in range(0, len(elements)):
            if elements[j] in i:
                vectList[j].append(int(i.get(elementList[j])))
            else:
                vectList[j].append(0)
    print(f'Vectors: {vectList}')
    return vectList


def createEquation(reacts, prods):
    # Combine reactant and product dictionaries into one list; order is preserved.
    compoundList = reacts + prods
    print(f'Combined: {compoundList}')
    # Get the union (merged dictionary) of all compound dictionaries.
    # Then extract the keys (unique element symbols) in a list.
    uniqueElements = list(mergeDicts(compoundList).keys())

    # Initialize a matrix with one row per unique element.
    # Each row will eventually have one entry per compound in compoundList.
    equations = [[] for _ in range(len(compoundList))]

    # Loop over each compound in our list...
    for j, compound in enumerate(compoundList):
        # For each unique element, insert the count (or 0 if missing)
        for i, elem in enumerate(uniqueElements):
            equations[j].append(int(compound.get(elem, 0)))

    return equations, compoundList

def solver(eqs):
    matrix = Matrix(eqs).transpose()

    nullSpace = matrix.nullspace()

    if not nullSpace:
        return False
    solution = nullSpace[0]
    i=1
    while 0 in solution and i < len(nullSpace):
        solution = nullSpace[i]
        i+=1

    lcmList = lcm([i.q for i in solution])

    solution = [int(i * lcmList) for i in solution]

    return solution

# Example usage:
matrix, compoundList = createEquation(oneSide(reactants), oneSide(products))
#print("Compound List:", compoundList)
#print(f'split value:{len(oneSide(reactants))-1}')
#print(matrix[len(oneSide(reactants))-1])
i = len(oneSide(reactants))
print(f'I Value: {i}')
while i < len(matrix):
    print(f'Matrix: {matrix[i]}')
    for j in range(len(matrix[i])):
        matrix[i][j] *= -1
    print(f'products: {matrix[i]}')
    i+=1
print(f'Final Matrix: {matrix}')
print(solver(matrix))
print(f'TEST!!!!! {oneSide(["Mg^4"])}')
