def solution():
    """Jose is a collector of fine wines. His private cellar currently holds 2400 bottles of imported wine and half as many bottles of domestic wine as imported wine. If Jose holds a party and the guests drink one-third of all his wine, how many bottles will remain in his cellar?"""
    # Define the initial number of imported wine bottles
    imported_wine = 2400

    # Calculate the number of domestic wine bottles
    domestic_wine = imported_wine / 2

    # Calculate the total number of wine bottles
    total_wine = imported_wine + domestic_wine

    # Calculate the number of wine bottles drank at the party
    drank_wine = total_wine / 3

    # Calculate the number of wine bottles remaining in the cellar
    remaining_wine = total_wine - drank_wine

    # return the result
    result = remaining_wine
    return result

print(solution())