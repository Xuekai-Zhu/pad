def solution():
    imported_wine = 2400  # Jose has 2400 bottles of imported wine
    domestic_wine = imported_wine / 2  # Jose has half as many bottles of domestic wine as imported wine
    total_wine = imported_wine + domestic_wine  # Total number of wine bottles in the cellar
    wine_consumed = total_wine / 3  # Guests drink one-third of all the wine

    # Calculate the number of wine bottles remaining in the cellar
    remaining_wine = total_wine - wine_consumed
    result = remaining_wine
    return result

print(solution())