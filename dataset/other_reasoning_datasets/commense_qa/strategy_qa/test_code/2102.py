def solution():
    peach_character = "Princess Peach"
    peach_skin_colors = ["red", "orange", "yellow"]
    peach_dress_color = "pink"
    if peach_dress_color in peach_skin_colors:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())