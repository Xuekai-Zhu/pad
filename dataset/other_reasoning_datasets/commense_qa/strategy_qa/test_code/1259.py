def solution():
    primary_colors = ["red", "green", "blue"]
    black_color = "absence of color"
    if set(primary_colors) == {"red", "green", "blue"} and black_color == "absence of color":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())