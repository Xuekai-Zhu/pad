def solution():
    """Jeff decides to install more cabinets in his kitchen. He currently has 3 cabinets over one counter and no other cabinets. He installs twice as many cabinets over 3 different counters each. He then installs 5 more cabinets. How many total cabinets does he have?"""
    # Define the initial number of cabinets
    initial_cabinets = 3

    # Calculate the number of cabinets installed over each counter
    counter_cabinets = 2 * initial_cabinets

    # Calculate the total number of cabinets installed
    total_cabinets = initial_cabinets + (3 * counter_cabinets) + 5

    result = total_cabinets
    return result

print(solution())