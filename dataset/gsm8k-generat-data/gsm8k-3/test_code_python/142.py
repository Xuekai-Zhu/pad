def solution():
    """A cleaning company produces two sanitizer sprays. One spray kills 50% of germs, and another spray kills 25% of germs. However, 5% of the germs they kill are the same ones. What percentage of germs would be left after using both sanitizer sprays together?"""
    # Define the initial percentage of germs
    initial_percentage = 100

    # Calculate the percentage of germs killed by the first spray
    first_spray_percentage = 50

    # Calculate the percentage of germs killed by the second spray
    second_spray_percentage = 25

    # Calculate the percentage of germs killed by both sprays
    both_sprays_percentage = (first_spray_percentage + second_spray_percentage) - (first_spray_percentage * second_spray_percentage * 5 / 100)

    # Calculate the percentage of germs left after using both sprays
    final_percentage = initial_percentage - both_sprays_percentage

    result = final_percentage
    return result

print(solution())