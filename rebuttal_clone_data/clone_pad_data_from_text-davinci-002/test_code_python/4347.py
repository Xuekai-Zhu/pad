def solution():
    knives = 24
    teaspoons = knives * 2
    additional_knives = knives / 3
    additional_teaspoons = teaspoons / 3
    total_knives = knives + additional_knives
    total_teaspoons = teaspoons + additional_teaspoons
    total_cutlery = total_knives + total_teaspoons
    result = total_cutlery
    return result

print(solution())