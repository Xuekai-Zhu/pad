def solution():
    # Calculate Johanna's number of turtles
    johanna_turtles = 21 - 5

    # Calculate Owen's new number of turtles after 1 month
    owen_turtles = 2 * 21

    # Calculate Johanna's new number of turtles after losing half and donating the rest
    johanna_turtles = johanna_turtles / 2

    # Add Johanna's remaining turtles to Owen's new number
    total_turtles = owen_turtles + johanna_turtles

    result = total_turtles
    return result

print(solution())