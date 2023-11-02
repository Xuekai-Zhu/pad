def solution():
    """Jeff decides to install more cabinets in his kitchen. He currently has 3 cabinets over one counter and no other cabinets. He installs twice as many cabinets over 3 different counters each. He then installs 5 more cabinets. How many total cabinets does he have?"""
    initial_cabinets = 3
    num_counters = 3
    additional_cabinets = num_counters * 2 * initial_cabinets
    total_cabinets = initial_cabinets + additional_cabinets + 5
    result = total_cabinets
    return result

print(solution())