def solution():
    
    knives = 24
    teaspoons = 2 * knives
    additional_knives = knives / 3
    additional_teaspoons = (2/3) * teaspoons
    total_cutlery = knives + teaspoons + additional_knives + additional_teaspoons
    result = total_cutlery
    return result

print(solution())