ogString = input("Enter the Equation (Write ^x for any subscript):")


def inputHandling(firstEquation):
    # Split Reaction into 2 Sides
    sides = firstEquation.split('=')
    reactants = sides[0].split('+')
    reactantSplit = []

    products = sides[1].split('+')
    productSplit = []

    # Parse Reactants into Lists
    for i in range(len(reactants)):
        # Remove spaces first, then convert to list
        reactantSplit.append(list(reactants[i].replace(" ", "")))

    reactantDict = dict()

    # Parse Reactant List into Dictionary with Values
    for x in range(len(reactantSplit)):
        for y in range(len(reactantSplit[x])):

            # If there is more than one of an atom in the compound
            if '^' in reactantSplit[x]:

                if y > 0 and y < len(reactantSplit[x]):
                    if reactantSplit[x][y] == '^':
                        # Remove the check for isupper() on the ^ character
                        if y > 1:
                            reactantDict.update(
                                {f'{reactantSplit[x][y - 2]}{reactantSplit[x][y - 1]}': int(reactantSplit[x][y + 1])})
                        else:
                            reactantDict.update({reactantSplit[x][y - 1]: int(reactantSplit[x][y + 1])})

            else:
                if y < len(reactantSplit[x]) - 1:  # Fixed boundary check
                    if reactantSplit[x][y].isupper() and reactantSplit[x][y+1].islower():
                        reactantDict.update(
                            {f'{reactantSplit[x][y]}{reactantSplit[x][y+1]}': 1})
                        reactantSplit[x][y+1] = '_'
                    elif reactantSplit[x][y].isupper():
                        reactantDict.update(
                            {reactantSplit[x][y]: 1})

    for i in range(len(products)):
        # Remove spaces first, then convert to list
        productSplit.append(list(products[i].replace(" ", "")))

    productDict = dict()

    for x in range(len(productSplit)):
        for y in range(len(productSplit[x])):
            if '^' in productSplit[x]:
                if y > 0 and y < len(productSplit[x]):
                    if productSplit[x][y] == '^':
                        if productSplit[x][y-1].isupper():
                            productDict.update({productSplit[x][y - 1]: int(productSplit[x][y + 1])})

                        else:
                            productDict.update({f'{productSplit[x][y-2]}{productSplit[x][y-1]}': int(productSplit[x][y + 1])})
                elif productSplit[x][y].isupper() and productSplit[x][y + 1].islower():
                    productDict.update({f'{productSplit[x][y]}{productSplit[x][y + 1]}': 1})

            else:
                if y < len(productSplit[x]) - 1:  # Fixed boundary check
                    if productSplit[x][y].isupper() and productSplit[x][y + 1].islower():
                        productDict.update(
                            {f'{productSplit[x][y]}{productSplit[x][y + 1]}': 1})
                        productSplit[x][y + 1] = '_'
                    elif productSplit[x][y].isupper():
                        productDict.update(
                            {productSplit[x][y]: 1})
    return reactantDict, productDict


print(inputHandling(ogString))
