def solution():
    """Martha is grinding a spice paste. She adds 3 tablespoons of ginger, 1 teaspoon of cardamom, 1 teaspoon of mustard, 2 tablespoons of garlic, and four times as much chile powder as mustard. What percentage of the spice paste is ginger, rounded to the nearest integer? (Remember there are three teaspoons per tablespoon.)"""
    
    # Calculate the total volume of the spice paste in tablespoons
    total_volume = 3 + (1/3) + (1/3) + 2 + (4/3)

    # Calculate the volume of ginger in tablespoons
    ginger_volume = 3

    # Calculate the percentage of the spice paste that is ginger
    ginger_percentage = (ginger_volume / total_volume) * 100

    # Round the percentage to the nearest integer
    rounded_percentage = round(ginger_percentage)

    # Display the rounded percentage
    result = rounded_percentage
    return result

print(solution())