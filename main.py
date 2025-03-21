ogString = input("Enter the Equation (Write ^x for any subscript):")


def inputHandling(firstEquation):
    # Split Reaction into 2 Sides
    sides = firstEquation.split('=')
    reactants = sides[0].split('+')
    reactantSplit = []
    reactantConsts = []

    products = sides[1].split('+')
    productSplit = []
    productConsts = []
    polyDict = dict()
    # Parse Reactants into Lists
    for i in range(len(reactants)):
        # Remove spaces first, then convert to list
        reactantSplit.append(list(reactants[i].replace(" ", "")))

    reactantDict = dict()

    # Parse Reactant List into Dictionary with Values
    for x in range(len(reactantSplit)):
        skip_next = False
        constants = 1
        if reactantSplit[x][0].isdigit():
            constants = int(reactantSplit[x][0])

        reactantConsts.append(constants)
        for y in range(len(reactantSplit[x])):
            if skip_next:
                skip_next = False
                continue

            polyatomic = False
            polyconstants = 1

            # If there is more than one of an atom in the compound
            if '^' in reactantSplit[x] and '(' not in reactantSplit[x]:
                if y > 0 and y < len(reactantSplit[x]):
                    if reactantSplit[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if reactantSplit[x][y - 1].islower() and y > 1:
                            if f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': int(
                                    reactantSplit[x][y + 1])*constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}')
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': existing + (int(reactantSplit[x][y + 1])*constants)})
                        else:
                            # Single letter element
                            if reactantSplit[x][y - 1] not in reactantDict:
                                reactantDict.update({reactantSplit[x][y - 1]: int(reactantSplit[x][y + 1])*constants})
                            else:
                                existing = reactantDict.get(reactantSplit[x][y - 1])
                                reactantDict.update({reactantSplit[x][y - 1]: existing + (int(reactantSplit[x][y + 1])*constants)})
            elif '^' in reactantSplit[x]:
                if y > 0 and y < len(reactantSplit[x]):
                    if reactantSplit[x][y] == '(':
                        polyatomic = True
                    if reactantSplit[x][reactantSplit[x].index(')') + 1] == '^':
                        polyconstants = reactantSplit[x][reactantSplit[x].index(')')+2]

                    if reactantSplit[x][y] == '^' and not polyatomic:
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if reactantSplit[x][y - 1].islower() and y > 1:
                            if f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': int(reactantSplit[x][y + 1])*constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}')
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': existing + (int(reactantSplit[x][y + 1])*constants)})
                        else:
                            # Single letter element
                            if reactantSplit[x][y - 1] not in reactantDict:
                                reactantDict.update({reactantSplit[x][y - 1]: int(reactantSplit[x][y + 1])*constants})
                            else:
                                existing = reactantDict.get(reactantSplit[x][y - 1])
                                reactantDict.update({reactantSplit[x][y - 1]: existing + (int(reactantSplit[x][y + 1])*constants)})
                    if y < reactantSplit[x].index('(') and y < reactantSplit[x].index(')'):
                        if reactantSplit[x][y - 1].islower() and y > 1:
                            if f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': int(
                                reactantSplit[x][y + 1])*constants * polyconstants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}')
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': existing + (int(reactantSplit[x][y + 1])*constants * polyconstants)})
                        else:
                            # Single letter element
                            if reactantSplit[x][y - 1] not in reactantDict:
                                reactantDict.update({reactantSplit[x][y - 1]: int(reactantSplit[x][y + 1])*constants * polyconstants})
                            else:
                                existing = reactantDict.get(reactantSplit[x][y - 1])
                                reactantDict.update({reactantSplit[x][y - 1]: existing + (int(reactantSplit[x][y + 1])*constants * polyconstants)})

            # Handle elements without subscripts
            if y < len(reactantSplit[x]) and reactantSplit[x][y].isupper() and '(' not in reactantSplit[x]:
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(reactantSplit[x]) and reactantSplit[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(reactantSplit[x]) or reactantSplit[x][y + 2] != '^':
                        if f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}' not in reactantDict:
                            reactantDict.update({f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}': constants})
                        else:
                            existing = reactantDict.get(f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}')
                            reactantDict.update({f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(reactantSplit[x]) or reactantSplit[x][y + 1] != '^':

                    if reactantSplit[x][y] not in reactantDict:
                        reactantDict.update({reactantSplit[x][y]: constants})

                    else:
                        existing = reactantDict.get(reactantSplit[x][y])
                        reactantDict.update({reactantSplit[x][y]: existing + constants})

    for i in range(len(products)):
        # Remove spaces first, then convert to list
        productSplit.append(list(products[i].replace(" ", "")))

    productDict = dict()

    # Using the same improved logic for products
    for x in range(len(productSplit)):
        skip_next = False
        constants = 1
        if productSplit[x][0].isdigit():
            constants = int(productSplit[x][0])

        productConsts.append(constants)
        for y in range(len(productSplit[x])):
            if skip_next:
                skip_next = False
                continue

            # If there is more than one of an atom in the compound
            if '^' in productSplit[x]:
                if y > 0 and y < len(productSplit[x]):
                    if productSplit[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if productSplit[x][y - 1].islower() and y > 1:
                            if f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}' not in productDict:
                                productDict.update({f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}': int(productSplit[x][y + 1])*constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = productDict.get(f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}')
                                productDict.update({f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}': existing + (int(productSplit[x][y + 1])*constants)})
                        else:
                            # Single letter element
                            if productSplit[x][y-1] not in productDict:
                                productDict.update({productSplit[x][y - 1]: int(productSplit[x][y + 1])*constants})
                            else:
                                existing = productDict.get(productSplit[x][y-1])
                                productDict.update({productSplit[x][y - 1]: existing + (int(productSplit[x][y + 1])*constants)})

            # Handle elements without subscripts
            if y < len(productSplit[x]) and productSplit[x][y].isupper():
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(productSplit[x]) and productSplit[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(productSplit[x]) or productSplit[x][y + 2] != '^':
                        if f'{productSplit[x][y]}{productSplit[x][y + 1]}' not in productDict:
                            productDict.update({f'{productSplit[x][y]}{productSplit[x][y + 1]}': constants})
                        else:
                            existing = productDict.get(f'{productSplit[x][y]}{productSplit[x][y + 1]}')
                            productDict.update({f'{productSplit[x][y]}{productSplit[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(productSplit[x]) or productSplit[x][y + 1] != '^':

                    if productSplit[x][y] not in productDict:
                        productDict.update({productSplit[x][y]: constants})

                    else:
                        existing = productDict.get(productSplit[x][y])
                        productDict.update({productSplit[x][y]: existing + constants})


    return reactantDict, productDict, reactantSplit, productSplit, reactantConsts, productConsts

def reCheck(reactDic, prodDic, prodParts, reactParts):
    reactantConsts = []
    productConsts = []

    for x in range(len(reactParts)):
        skip_next = False
        for y in range(len(reactParts[x])):
            if skip_next:
                skip_next = False
                continue

            # If there is more than one of an atom in the compound
            constants = 1
            if reactParts[x][0].isdigit():
                constants = int(reactParts[x][0])

            reactantConsts.append(constants)

            if '^' in reactParts[x]:
                if y > 0 and y < len(reactParts[x]):
                    if reactParts[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if reactParts[x][y - 1].islower() and y > 1:
                            if f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}': int(
                                    reactParts[x][y + 1]) * constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}')
                                reactantDict.update({f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}': existing + (constants * int(reactParts[x][y + 1]))})
                        else:
                            # Single letter element
                            if reactParts[x][y - 1] not in reactantDict:
                                reactantDict.update({reactParts[x][y - 1]: int(reactParts[x][y + 1]) * constants})
                            else:
                                existing = reactantDict.get(reactParts[x][y - 1])
                                reactantDict.update({reactParts[x][y - 1]: existing + (int(reactParts[x][y + 1]) * constants)})

            # Handle elements without subscripts
            if y < len(reactParts[x]) and reactParts[x][y].isupper():
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(reactParts[x]) and reactParts[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(reactParts[x]) or reactParts[x][y + 2] != '^':
                        if f'{reactParts[x][y]}{reactParts[x][y + 1]}' not in reactantDict:
                            reactantDict.update({f'{reactParts[x][y]}{reactParts[x][y + 1]}': constants})
                        else:
                            existing = reactantDict.get(f'{reactParts[x][y]}{reactParts[x][y + 1]}')
                            reactantDict.update({f'{reactParts[x][y]}{reactParts[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(reactParts[x]) or reactParts[x][y + 1] != '^':

                    if reactParts[x][y] not in reactantDict:
                        reactantDict.update({reactParts[x][y]: constants})

                    else:
                        existing = reactantDict.get(reactParts[x][y])
                        reactantDict.update({reactParts[x][y]: existing + constants})


    productDict = dict()

    # Using the same improved logic for products
    for x in range(len(prodParts)):
        skip_next = False
        for y in range(len(prodParts[x])):
            if skip_next:
                skip_next = False
                continue

            constants = 1
            if prodParts[x][0].isdigit():
                constants = int(prodParts[x][0])

            productConsts.append(constants)
            # If there is more than one of an atom in the compound
            if '^' in prodParts[x] and '(' not in prodParts[x]:
                if y > 0 and y < len(prodParts[x]):
                    if prodParts[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if prodParts[x][y - 1].islower() and y > 1:
                            if f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}' not in productDict:
                                productDict.update({f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}': int(prodParts[x][y + 1])* constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = productDict.get(f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}')
                                productDict.update({f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}': existing + (int(prodParts[x][y + 1])* constants)})
                        else:
                            # Single letter element
                            if prodParts[x][y-1] not in productDict:
                                productDict.update({prodParts[x][y - 1]: int(prodParts[x][y + 1])* constants})
                            else:
                                existing = productDict.get(prodParts[x][y-1])
                                productDict.update({prodParts[x][y - 1]: existing + (int(prodParts[x][y + 1])* constants)})

            # Handle elements without subscripts
            if y < len(prodParts[x]) and prodParts[x][y].isupper() and '(' not in prodParts[x]:
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(prodParts[x]) and prodParts[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(prodParts[x]) or prodParts[x][y + 2] != '^':
                        if f'{prodParts[x][y]}{prodParts[x][y + 1]}' not in productDict:
                            productDict.update({f'{prodParts[x][y]}{prodParts[x][y + 1]}': constants})
                        else:
                            existing = productDict.get(f'{prodParts[x][y]}{prodParts[x][y + 1]}')
                            productDict.update({f'{prodParts[x][y]}{prodParts[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(prodParts[x]) or prodParts[x][y + 1] != '^':

                    if prodParts[x][y] not in productDict:
                        productDict.update({prodParts[x][y]: constants})

                    else:
                        existing = productDict.get(prodParts[x][y])
                        productDict.update({prodParts[x][y]: existing + constants})


    return reactantDict, productDict, reactParts, prodParts, reactantConsts, productConsts

def balanceCheck(reactDic, prodDic):
    solved = 0
    for x in reactDic:
        if reactDic.get(x) == prodDic.get(x):
            solved += 1

    if solved == len(reactDic):
        return True
    else:
        return False
def solver(reactDic, prodDic, reactParts, prodParts, reactConsts, prodConsts):
    values = dict()
    letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z'}
    for i in prodParts:
        values.update({letters[i]: 1})
reactantDict, productDict, reactantParts, productParts, reactantConsts, productConsts = inputHandling(ogString)

print(balanceCheck(reactantDict, productDict))
print(inputHandling(ogString))ogString = input("Enter the Equation (Write ^x for any subscript):")


def inputHandling(firstEquation):
    # Split Reaction into 2 Sides
    sides = firstEquation.split('=')
    reactants = sides[0].split('+')
    reactantSplit = []
    reactantConsts = []

    products = sides[1].split('+')
    productSplit = []
    productConsts = []
    polyDict = dict()
    # Parse Reactants into Lists
    for i in range(len(reactants)):
        # Remove spaces first, then convert to list
        reactantSplit.append(list(reactants[i].replace(" ", "")))

    reactantDict = dict()

    # Parse Reactant List into Dictionary with Values
    for x in range(len(reactantSplit)):
        skip_next = False
        constants = 1
        if reactantSplit[x][0].isdigit():
            constants = int(reactantSplit[x][0])

        reactantConsts.append(constants)
        for y in range(len(reactantSplit[x])):
            if skip_next:
                skip_next = False
                continue

            polyatomic = False
            polyconstants = 1

            # If there is more than one of an atom in the compound
            if '^' in reactantSplit[x] and '(' not in reactantSplit[x]:
                if y > 0 and y < len(reactantSplit[x]):
                    if reactantSplit[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if reactantSplit[x][y - 1].islower() and y > 1:
                            if f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': int(
                                    reactantSplit[x][y + 1])*constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}')
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': existing + (int(reactantSplit[x][y + 1])*constants)})
                        else:
                            # Single letter element
                            if reactantSplit[x][y - 1] not in reactantDict:
                                reactantDict.update({reactantSplit[x][y - 1]: int(reactantSplit[x][y + 1])*constants})
                            else:
                                existing = reactantDict.get(reactantSplit[x][y - 1])
                                reactantDict.update({reactantSplit[x][y - 1]: existing + (int(reactantSplit[x][y + 1])*constants)})
            elif '^' in reactantSplit[x]:
                if y > 0 and y < len(reactantSplit[x]):
                    if reactantSplit[x][y] == '(':
                        polyatomic = True
                    if reactantSplit[x][reactantSplit[x].index(')') + 1] == '^':
                        polyconstants = reactantSplit[x][reactantSplit[x].index(')')+2]
                    if reactantSplit[x][y] == '^' and not polyatomic:
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if reactantSplit[x][y - 1].islower() and y > 1:
                            if f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': int(
                                    reactantSplit[x][y + 1])*constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}')
                                reactantDict.update({f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': existing + (int(reactantSplit[x][y + 1])*constants)})
                        else:
                            # Single letter element
                            if reactantSplit[x][y - 1] not in reactantDict:
                                reactantDict.update({reactantSplit[x][y - 1]: int(reactantSplit[x][y + 1])*constants})
                            else:
                                existing = reactantDict.get(reactantSplit[x][y - 1])
                                reactantDict.update({reactantSplit[x][y - 1]: existing + (int(reactantSplit[x][y + 1])*constants)})

            # Handle elements without subscripts
            if y < len(reactantSplit[x]) and reactantSplit[x][y].isupper() and '(' not in reactantSplit[x]:
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(reactantSplit[x]) and reactantSplit[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(reactantSplit[x]) or reactantSplit[x][y + 2] != '^':
                        if f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}' not in reactantDict:
                            reactantDict.update({f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}': constants})
                        else:
                            existing = reactantDict.get(f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}')
                            reactantDict.update({f'{reactantSplit[x][y]}{reactantSplit[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(reactantSplit[x]) or reactantSplit[x][y + 1] != '^':

                    if reactantSplit[x][y] not in reactantDict:
                        reactantDict.update({reactantSplit[x][y]: constants})

                    else:
                        existing = reactantDict.get(reactantSplit[x][y])
                        reactantDict.update({reactantSplit[x][y]: existing + constants})

    for i in range(len(products)):
        # Remove spaces first, then convert to list
        productSplit.append(list(products[i].replace(" ", "")))

    productDict = dict()

    # Using the same improved logic for products
    for x in range(len(productSplit)):
        skip_next = False
        constants = 1
        if productSplit[x][0].isdigit():
            constants = int(productSplit[x][0])

        productConsts.append(constants)
        for y in range(len(productSplit[x])):
            if skip_next:
                skip_next = False
                continue

            # If there is more than one of an atom in the compound
            if '^' in productSplit[x]:
                if y > 0 and y < len(productSplit[x]):
                    if productSplit[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if productSplit[x][y - 1].islower() and y > 1:
                            if f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}' not in productDict:
                                productDict.update({f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}': int(productSplit[x][y + 1])*constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = productDict.get(f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}')
                                productDict.update({f'{productSplit[x][y - 2]}{productSplit[x][y - 1]}': existing + (int(productSplit[x][y + 1])*constants)})
                        else:
                            # Single letter element
                            if productSplit[x][y-1] not in productDict:
                                productDict.update({productSplit[x][y - 1]: int(productSplit[x][y + 1])*constants})
                            else:
                                existing = productDict.get(productSplit[x][y-1])
                                productDict.update({productSplit[x][y - 1]: existing + (int(productSplit[x][y + 1])*constants)})

            # Handle elements without subscripts
            if y < len(productSplit[x]) and productSplit[x][y].isupper():
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(productSplit[x]) and productSplit[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(productSplit[x]) or productSplit[x][y + 2] != '^':
                        if f'{productSplit[x][y]}{productSplit[x][y + 1]}' not in productDict:
                            productDict.update({f'{productSplit[x][y]}{productSplit[x][y + 1]}': constants})
                        else:
                            existing = productDict.get(f'{productSplit[x][y]}{productSplit[x][y + 1]}')
                            productDict.update({f'{productSplit[x][y]}{productSplit[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(productSplit[x]) or productSplit[x][y + 1] != '^':

                    if productSplit[x][y] not in productDict:
                        productDict.update({productSplit[x][y]: constants})

                    else:
                        existing = productDict.get(productSplit[x][y])
                        productDict.update({productSplit[x][y]: existing + constants})


    return reactantDict, productDict, reactantSplit, productSplit, reactantConsts, productConsts

def reCheck(reactDic, prodDic, prodParts, reactParts):
    reactantConsts = []
    productConsts = []

    for x in range(len(reactParts)):
        skip_next = False
        for y in range(len(reactParts[x])):
            if skip_next:
                skip_next = False
                continue

            # If there is more than one of an atom in the compound
            constants = 1
            if reactParts[x][0].isdigit():
                constants = int(reactParts[x][0])

            reactantConsts.append(constants)

            if '^' in reactParts[x]:
                if y > 0 and y < len(reactParts[x]):
                    if reactParts[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if reactParts[x][y - 1].islower() and y > 1:
                            if f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}' not in reactantDict:
                                reactantDict.update({f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}': int(
                                    reactParts[x][y + 1]) * constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = reactantDict.get(f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}')
                                reactantDict.update({f'{reactParts[x][y - 2]}{reactParts[x][y - 1]}': existing + (constants * int(reactParts[x][y + 1]))})
                        else:
                            # Single letter element
                            if reactParts[x][y - 1] not in reactantDict:
                                reactantDict.update({reactParts[x][y - 1]: int(reactParts[x][y + 1]) * constants})
                            else:
                                existing = reactantDict.get(reactParts[x][y - 1])
                                reactantDict.update({reactParts[x][y - 1]: existing + (int(reactParts[x][y + 1]) * constants)})

            # Handle elements without subscripts
            if y < len(reactParts[x]) and reactParts[x][y].isupper():
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(reactParts[x]) and reactParts[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(reactParts[x]) or reactParts[x][y + 2] != '^':
                        if f'{reactParts[x][y]}{reactParts[x][y + 1]}' not in reactantDict:
                            reactantDict.update({f'{reactParts[x][y]}{reactParts[x][y + 1]}': constants})
                        else:
                            existing = reactantDict.get(f'{reactParts[x][y]}{reactParts[x][y + 1]}')
                            reactantDict.update({f'{reactParts[x][y]}{reactParts[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(reactParts[x]) or reactParts[x][y + 1] != '^':

                    if reactParts[x][y] not in reactantDict:
                        reactantDict.update({reactParts[x][y]: constants})

                    else:
                        existing = reactantDict.get(reactParts[x][y])
                        reactantDict.update({reactParts[x][y]: existing + constants})


    productDict = dict()

    # Using the same improved logic for products
    for x in range(len(prodParts)):
        skip_next = False
        for y in range(len(prodParts[x])):
            if skip_next:
                skip_next = False
                continue

            constants = 1
            if prodParts[x][0].isdigit():
                constants = int(prodParts[x][0])

            productConsts.append(constants)
            # If there is more than one of an atom in the compound
            if '^' in prodParts[x] and '(' not in prodParts[x]:
                if y > 0 and y < len(prodParts[x]):
                    if prodParts[x][y] == '^':
                        # Check if character before ^ is uppercase (single element) or lowercase (part of two-letter element)
                        if prodParts[x][y - 1].islower() and y > 1:
                            if f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}' not in productDict:
                                productDict.update({f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}': int(prodParts[x][y + 1])* constants})
                            # Two-letter element (like 'Cl' in 'ZnCl^2')
                            else:
                                existing = productDict.get(f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}')
                                productDict.update({f'{prodParts[x][y - 2]}{prodParts[x][y - 1]}': existing + (int(prodParts[x][y + 1])* constants)})
                        else:
                            # Single letter element
                            if prodParts[x][y-1] not in productDict:
                                productDict.update({prodParts[x][y - 1]: int(prodParts[x][y + 1])* constants})
                            else:
                                existing = productDict.get(prodParts[x][y-1])
                                productDict.update({prodParts[x][y - 1]: existing + (int(prodParts[x][y + 1])* constants)})

            # Handle elements without subscripts
            if y < len(prodParts[x]) and prodParts[x][y].isupper() and '(' not in prodParts[x]:
                # Check if this is followed by a lowercase letter (two-letter element)
                if y + 1 < len(prodParts[x]) and prodParts[x][y + 1].islower():
                    # Check if this is already processed by ^ handling
                    if y + 2 >= len(prodParts[x]) or prodParts[x][y + 2] != '^':
                        if f'{prodParts[x][y]}{prodParts[x][y + 1]}' not in productDict:
                            productDict.update({f'{prodParts[x][y]}{prodParts[x][y + 1]}': constants})
                        else:
                            existing = productDict.get(f'{prodParts[x][y]}{prodParts[x][y + 1]}')
                            productDict.update({f'{prodParts[x][y]}{prodParts[x][y + 1]}': existing + constants})

                        skip_next = True
                # Single letter element not followed by ^
                elif y + 1 >= len(prodParts[x]) or prodParts[x][y + 1] != '^':

                    if prodParts[x][y] not in productDict:
                        productDict.update({prodParts[x][y]: constants})

                    else:
                        existing = productDict.get(prodParts[x][y])
                        productDict.update({prodParts[x][y]: existing + constants})


    return reactantDict, productDict, reactParts, prodParts, reactantConsts, productConsts

def balanceCheck(reactDic, prodDic):
    solved = 0
    for x in reactDic:
        if reactDic.get(x) == prodDic.get(x):
            solved += 1

    if solved == len(reactDic):
        return True
    else:
        return False
def solver(reactDic, prodDic, reactParts, prodParts, reactConsts, prodConsts):
    values = dict()
    letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z'}
    for i in prodParts:
        values.update({letters[i]: 1})
reactantDict, productDict, reactantParts, productParts, reactantConsts, productConsts = inputHandling(ogString)

print(balanceCheck(reactantDict, productDict))
print(inputHandling(ogString))
