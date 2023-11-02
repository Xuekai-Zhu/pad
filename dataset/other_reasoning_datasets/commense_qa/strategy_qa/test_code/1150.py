def solution():
    lg_location = "Seoul"
    city_bird_colors = {"Seoul": ["purple", "blue"]}
    if lg_location in city_bird_colors.keys() and "purple" in city_bird_colors[lg_location] and "blue" in city_bird_colors[lg_location]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())