def solution():
    """Jeff decides to install more cabinets in his kitchen. He currently has 3 cabinets over one counter and no other cabinets. He installs twice as many cabinets over 3 different counters each. He then installs 5 more cabinets. How many total cabinets does he have?"""
    starting_cabinets = 3
    additional_cabinets_per_counter = 2 * starting_cabinets
    counters = 3
    total_additional_cabinets = additional_cabinets_per_counter * counters
    additional_cabinets = 5
    total_cabinets = starting_cabinets + total_additional_cabinets + additional_cabinets
    result = total_cabinets
    return result

print(solution())