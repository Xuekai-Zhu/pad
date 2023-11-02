def solution():
    """A flagpole is 12 feet tall. It breaks, folding over in half, such that what was the tip of the flagpole is now dangling two feet above the ground. How far from the base, in feet, did the flagpole break?"""
    # Determine the length of the top portion of the flagpole
    top_length = 12 / 2 - 2

    # Use the Pythagorean theorem to calculate the distance from the base
    # of the flagpole to where it broke
    distance = (top_length ** 2 + 6 ** 2) ** 0.5

    # Display the distance from the base
    result = distance
    return result

print(solution())