def solution():
    """A flagpole is 12 feet tall. It breaks, folding over in half, such that what was the tip of the flagpole is now dangling two feet above the ground. How far from the base, in feet, did the flagpole break?"""
    # Define the height of the flagpole and the distance from the base where it broke
    flagpole_height = 12
    break_distance = None

    # Calculate the distance from the base of the flagpole where it broke
    break_distance = (flagpole_height**2 - 2**2)**0.5

    # return the result
    result = break_distance
    return result

print(solution())