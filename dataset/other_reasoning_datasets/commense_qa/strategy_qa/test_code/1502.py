def solution():
    animal_habitat = "trees"
    animal_coat_colors = ["black", "white"]
    if len(animal_coat_colors) > 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())