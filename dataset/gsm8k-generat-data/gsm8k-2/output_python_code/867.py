def solution():
    """A flagpole is 12 feet tall. It breaks, folding over in half, such that what was the tip of the flagpole is now dangling two feet above the ground. How far from the base, in feet, did the flagpole break?"""
    flagpole_height = 12
    tip_dangling_height = 2
    broken_height = flagpole_height - tip_dangling_height
    distance_from_base = broken_height / 2
    result = distance_from_base
    return result

print(solution())