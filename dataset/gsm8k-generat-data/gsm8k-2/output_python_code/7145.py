def solution():
    """Martha is grinding a spice paste. She adds 3 tablespoons of ginger, 1 teaspoon of cardamom, 1 teaspoon of mustard,
    2 tablespoons of garlic, and four times as much chile powder as mustard. What percentage of the spice paste is ginger,
    rounded to the nearest integer? (Remember there are three teaspoons per tablespoon.)"""
    ginger = 3 * 3  # convert tablespoons to teaspoons
    mustard = 1
    chile = 4 * mustard
    total_spice = ginger + mustard + chile + 2 * 3  # add teaspoons of cardamom and garlic (2 tablespoons)
    ginger_percentage = (ginger / total_spice) * 100
    result = round(ginger_percentage)
    return result

print(solution())