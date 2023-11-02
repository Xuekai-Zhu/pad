def solution():
    american_flag_colors = ["red", "white", "blue"]
    mickey_mouse_colors = ["red", "yellow", "white"]
    similar_colors = set(american_flag_colors) & set(mickey_mouse_colors)
    if similar_colors:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())