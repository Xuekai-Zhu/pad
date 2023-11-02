def solution():
    """Martha is grinding a spice paste. She adds 3 tablespoons of ginger, 1 teaspoon of cardamom, 1 teaspoon of mustard, 2 tablespoons of garlic, and four times as much chile powder as mustard. What percentage of the spice paste is ginger, rounded to the nearest integer? (Remember there are three teaspoons per tablespoon.)"""
    # Define the amount of each spice added
    ginger = 3 * 3 # three teaspoons per tablespoon
    cardamom = 1
    mustard = 1
    garlic = 2 * 3 # three teaspoons per tablespoon
    chile_powder = 4 * mustard

    # Calculate the total amount of spice paste
    total_spice = ginger + cardamom + mustard + garlic + chile_powder

    # Calculate the percentage of the spice paste that is ginger
    ginger_percentage = (ginger / total_spice) * 100

    # Round the percentage to the nearest integer
    rounded_percentage = round(ginger_percentage)

    # Return the result
    result = rounded_percentage
    return result

print(solution())