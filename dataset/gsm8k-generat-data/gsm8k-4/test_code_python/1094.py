def solution():
    """Janice adds 2 tablespoons of koolaid power and 16 tablespoons of water to a jug.
    She leaves it out long enough for 4 tablespoons of water to evaporate.
    Then she quadruples the amount of water in the jug.
    What percentage of the liquid in the jug is koolaid powder?"""
    # Define the initial amount of koolaid powder and water
    initial_koolaid = 2
    initial_water = 16

    # Calculate the amount of water after evaporation
    remaining_water = initial_water - 4

    # Calculate the total amount of liquid in the jug after quadrupling the water
    total_liquid = remaining_water * 4 + initial_koolaid

    # Calculate the percentage of the liquid that is koolaid powder
    koolaid_percentage = (initial_koolaid / total_liquid) * 100

    result = koolaid_percentage
    return result

print(solution())