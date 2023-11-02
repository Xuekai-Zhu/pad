def solution():
    """Jan's three-eyed lizard has 3 times more wrinkles than eyes, and seven times more spots than wrinkles. How many fewer eyes does the lizard have than the combined number of spots and wrinkles?"""
    # Calculate the number of eyes
    eyes = 3

    # Calculate the number of wrinkles
    wrinkles = eyes * 3

    # Calculate the number of spots
    spots = wrinkles * 7

    # Calculate the combined number of spots and wrinkles
    combined = wrinkles + spots

    # Calculate the difference between eyes and the combined number of spots and wrinkles
    difference = combined - eyes

    # Display the result
    result = difference
    return result

print(solution())