def solution():
    sand_cat_prey = ["insects", "birds", "hares", "reptiles"]
    eel_prey = ["fish", "worms", "frogs", "lizards"]
    overlap = set(sand_cat_prey) & set(eel_prey)
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())