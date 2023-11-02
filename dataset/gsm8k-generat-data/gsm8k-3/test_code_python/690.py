def solution():
    """Jose is a collector of fine wines.  His private cellar currently holds 2400 bottles of imported wine and half as many bottles of domestic wine as imported wine.  If Jose holds a party and the guests drink one-third of all his wine, how many bottles will remain in his cellar?"""
    # Define the number of bottles of imported wine and domestic wine
    imported_wine = 2400
    domestic_wine = imported_wine / 2

    # Calculate the total number of bottles of wine
    total_wine = imported_wine + domestic_wine

    # Calculate the number of bottles of wine remaining after the party
    remaining_wine = total_wine - (total_wine / 3)

    # Display the number of bottles of wine remaining
    result = remaining_wine
    return result

print(solution())