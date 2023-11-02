def solution():
    """Jeff decides to install more cabinets in his kitchen. He currently has 3 cabinets over one counter and no other cabinets. He installs twice as many cabinets over 3 different counters each. He then installs 5 more cabinets. How many total cabinets does he have?"""
    # Define the initial number of cabinets
    initial_cabinets = 3

    # Define the number of cabinets installed over each of the 3 counters
    new_cabinets_per_counter = 2

    # Calculate the total number of cabinets installed over the 3 counters
    new_cabinets = new_cabinets_per_counter * 3

    # Calculate the total number of cabinets
    total_cabinets = initial_cabinets + new_cabinets + 5

    # Display the total number of cabinets
    result = total_cabinets
    return result

print(solution())