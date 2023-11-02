def solution():
    starting_bones = 10  # Barkley starts with 10 bones
    bones_available = 8  # After 5 months, Barkley has 8 bones available
    months_passed = 5  # Barkley has buried bones for 5 months

    # Calculate the total number of bones Barkley has buried
    buried_bones = starting_bones * months_passed - bones_available
    result = buried_bones
    return result

print(solution())