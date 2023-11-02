def solution():
    marlboro_colors = ["red", "white", "black"]
    french_flag_colors = ["red", "white", "blue"]
    overlap = [color for color in marlboro_colors if color in french_flag_colors]
    if len(overlap) == len(marlboro_colors):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())