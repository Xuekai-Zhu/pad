def solution():
    """Jan's three-eyed lizard has 3 times more wrinkles than eyes, and seven times more spots than wrinkles. How many fewer eyes does the lizard have than the combined number of spots and wrinkles?"""
    num_eyes = 3
    num_wrinkles = num_eyes * 3
    num_spots = num_wrinkles * 7
    total_spots_wrinkles = num_spots + num_wrinkles
    difference = total_spots_wrinkles - num_eyes
    result = difference
    return result

print(solution())