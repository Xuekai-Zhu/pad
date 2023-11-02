def solution():
    """A flagpole is 12 feet tall. It breaks, folding over in half, such that what was the tip of the flagpole is now dangling two feet above the ground. How far from the base, in feet, did the flagpole break?"""
    total_pole_length = 12
    remaining_length = total_pole_length / 2 + 2
    distance_from_base = total_pole_length - remaining_length
    result = distance_from_base
    return result

print(solution())