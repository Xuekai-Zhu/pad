def solution():
    
    # Define the fractions of each person that dresses in purple and blue
    PURPLE_FRACTION = 3/4
    BLUE_FRACTION = 1/4

    # Calculate the total fraction of the octuplets that dresses
    purple_fraction = PURPLE_FRACTION + BLUE_FRACTION
    blue_fraction = BLUE_FRACTION / 3

    # Calculate the total fraction of the octuplets that dresses
    total_fraction = purple_fraction + blue_fraction

    # Calculate the fraction of the octuplets that wear bows
    bow_fraction = 1/3

    # Calculate the total fraction of the octuplets that wear bows
    bows_fraction = 1 - bow_fraction

    # Calculate the percentage chance of a baby wearing a bow
    baby_percentage = (purple_fraction / total_fraction) * 100

    # Display the percentage chance of a baby wearing a bow
    result = baby_percentage
    return result

print(solution())