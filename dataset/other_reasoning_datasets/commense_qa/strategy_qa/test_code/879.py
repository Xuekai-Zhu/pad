def solution():
    rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    gabon_colors = ["green", "yellow", "blue"]
    overlap = [color for color in gabon_colors if color in rainbow_colors]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())