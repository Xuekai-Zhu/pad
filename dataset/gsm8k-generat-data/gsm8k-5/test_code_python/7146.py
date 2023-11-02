def solution():
    ginger = 3 * 3  # Convert 3 tablespoons to teaspoons
    cardamom = 1
    mustard = 1
    garlic = 2 * 3  # Convert 2 tablespoons to teaspoons
    chile_powder = 4 * mustard  # Four times as much as mustard

    total_spice = ginger + cardamom + mustard + garlic + chile_powder
    percentage_ginger = (ginger / total_spice) * 100

    result = round(percentage_ginger)
    return result

print(solution())