from sympy import Matrix, lcm

ogString = input("Enter the Equation (Write ^x for any subscript):")

# H(CO)^2 = H + C^2 + O^2
sides = ogString.split('=')
reactants = sides[0].split('+')
products = sides[1].split('+')


def oneSide(side):
    sideSplit = []
    sideVals = []

    for i in range(len(side)):
        # Remove spaces first, then convert to list
        sideSplit.append(list(side[i].replace(" ", "")))
        sideVals.append(dict())

    for counter, comp in enumerate(sideSplit):
        i = 0
        const = 1  # Default constant if none provided
        stack = []  # Stack to handle brackets
        temp_dict = {}  # Temporary dictionary for parsed elements

        while i < len(comp):
            if comp[i] == '(':
                polyco = True
                # Push current temp_dict and const to stack
                stack.append((temp_dict, const))
                temp_dict = {}
                const = 1
                i += 1
            elif comp[i] == ')':
                # Process the closing bracket
                i += 1
                multiplier = ''
                while i < len(comp) and comp[i].isdigit():
                    multiplier += comp[i]
                    i += 1
                multiplier = int(multiplier) if multiplier else 1
                # Multiply elements inside brackets by the multiplier
                for key in temp_dict:
                    temp_dict[key] *= multiplier
                # Pop the previous dictionary and merge
                prev_dict, prev_const = stack.pop()
                for key, value in temp_dict.items():
                    if key in prev_dict:
                        prev_dict[key] += value
                    else:
                        prev_dict[key] = value
                temp_dict = prev_dict
                const = prev_const
            elif comp[i].isdigit():
                # Handle leading coefficients (e.g., "2Mg^4")
                const = ''
                while i < len(comp) and comp[i].isdigit():
                    const += comp[i]
                    i += 1
                const = int(const)
            elif comp[i].isupper() and not polyco:
                # Parse elements
                element = comp[i]
                if i + 1 < len(comp) and comp[i + 1].islower():
                    element += comp[i + 1]
                    i += 1
                i += 1
                # Parse subscripts
                subscript = ''
                if i < len(comp) and comp[i] == '^':
                    i += 1
                    while i < len(comp) and comp[i].isdigit():
                        subscript += comp[i]
                        i += 1
                    subscript = int(subscript)
                else:
                    subscript = 1
                # Update the temporary dictionary
                if element in temp_dict:
                    temp_dict[element] += const * subscript
                else:
                    temp_dict[element] = const * subscript
                    
            elif comp[i].isupper() and polyco:
                # Parse elements
                element = comp[i]
                if i + 1 < len(comp) and comp[i + 1].islower():
                    element += comp[i + 1]
                    i += 1
                i += 1
                # Parse subscripts
                subscript = ''
                if i < len(comp) and comp[i] == '^':
                    i += 1
                    while i < len(comp) and comp[i].isdigit():
                        subscript += comp[i]
                        i += 1
                    subscript = int(subscript)
                else:
                    subscript = 1
                # Update the temporary dictionary
                if element in temp_dict:
                    temp_dict[element] += const * subscript
                else:
                    temp_dict[element] = const * subscript
            else:
                # Move to the next character
                i += 1

        # Merge the parsed dictionary into sideVals
        sideVals[counter] = temp_dict

    return sideVals


def mergeDicts(dicts):
    # print('Merging...')
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
    i = 1
    while 0 in solution and i < len(nullSpace):
        solution = nullSpace[i]
        i += 1

    lcmList = lcm([i.q for i in solution])

    solution = [int(i * lcmList) for i in solution]

    return solution


# Example usage:
matrix, compoundList = createEquation(oneSide(reactants), oneSide(products))
# print("Compound List:", compoundList)
# print(f'split value:{len(oneSide(reactants))-1}')
# print(matrix[len(oneSide(reactants))-1])
i = len(oneSide(reactants))
print(f'I Value: {i}')
while i < len(matrix):
    print(f'Matrix: {matrix[i]}')
    for j in range(len(matrix[i])):
        matrix[i][j] *= -1
    print(f'products: {matrix[i]}')
    i += 1
print(f'Final Matrix: {matrix}')
print(solver(matrix))
