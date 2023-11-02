def solution():
    """Janice adds 2 tablespoons of koolaid powder and 16 tablespoons of water to a jug. She leaves it out long enough for 4 tablespoons of water to evaporate. Then she quadruples the amount of water in the jug. What percentage of the liquid in the jug is koolaid powder?"""
    # Define the initial amount of koolaid powder and water
    INITIAL_KOOLAID = 2
    INITIAL_WATER = 16

    # Calculate the amount of water left after evaporation
    remaining_water = INITIAL_WATER - 4

    # Calculate the total amount of liquid in the jug after quadrupling the amount of water
    total_liquid = remaining_water * 4 + INITIAL_KOOLAID

    # Calculate the percentage of the liquid that is koolaid powder
    koolaid_percentage = (INITIAL_KOOLAID / total_liquid) * 100

    # Display the percentage of koolaid powder in the jug
    result = koolaid_percentage
    return result

print(solution())