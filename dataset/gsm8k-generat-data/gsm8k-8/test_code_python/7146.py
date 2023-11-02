def solution():
    # Calculate the total amount of spice paste in teaspoons
    ginger = 3 * 3
    cardamom = 1
    mustard = 1
    garlic = 2 * 3
    chile_powder = 4 * mustard
    total_spice = ginger + cardamom + mustard + garlic + chile_powder

    # Calculate the percentage of the spice paste that is ginger
    ginger_percent = (ginger / total_spice) * 100

    # Round the percentage to the nearest integer
    rounded_percent = round(ginger_percent)

    result = rounded_percent
    return result

print(solution())