def solution():
    primary_colors = ["red", "blue", "yellow"]
    blue_position = 1
    expensive_color = "ultramarine"
    expensive_color_ranking = 1
    if primary_colors[blue_position] == "blue" and expensive_color_ranking == 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())