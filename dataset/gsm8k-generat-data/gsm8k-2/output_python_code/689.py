def solution():
    """Jose is a collector of fine wines. His private cellar currently holds 2400 bottles of imported wine and half as many bottles of domestic wine as imported wine. If Jose holds a party and the guests drink one-third of all his wine, how many bottles will remain in his cellar?"""
    imported_wine = 2400
    domestic_wine = imported_wine / 2
    total_wine = imported_wine + domestic_wine
    wine_consumed = total_wine / 3
    wine_remaining = total_wine - wine_consumed
    result = wine_remaining
    return result

print(solution())