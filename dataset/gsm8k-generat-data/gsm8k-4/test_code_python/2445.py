def solution():
    """Jan's three-eyed lizard has 3 times more wrinkles than eyes, and seven times more spots than wrinkles. How many fewer eyes does the lizard have than the combined number of spots and wrinkles?"""
    # Define the ratio between eyes and wrinkles, and calculate the number of eyes
    eye_wrinkle_ratio = 1 / 3
    eyes = 3
    wrinkles = eyes * 3

    # Calculate the number of spots
    spots = wrinkles * 7

    # Calculate the combined number of spots and wrinkles
    total_spots_wrinkles = spots + wrinkles

    # Calculate the difference between eyes and the combined number of spots and wrinkles
    difference = total_spots_wrinkles - eyes

    # Return the result
    result = difference
    return result

print(solution())