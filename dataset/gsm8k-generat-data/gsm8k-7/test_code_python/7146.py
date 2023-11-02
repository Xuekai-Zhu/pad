def solution():
    ginger = 3 * 3  # Convert tablespoons to teaspoons
    cardamom = 1
    mustard = 1
    garlic = 2 * 3  # Convert tablespoons to teaspoons
    chile_powder = mustard * 4

    total_spice = ginger + cardamom + mustard + garlic + chile_powder

    percentage_ginger = (ginger / total_spice) * 100
    rounded_percentage_ginger = round(percentage_ginger)

    result = rounded_percentage_ginger
    return result

print(solution())