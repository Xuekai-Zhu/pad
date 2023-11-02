def solution():
    two_thirds = 2 / 3
    cats = two_thirds * 300
    dogs = 300 - cats
    legs_per_cat = 4
    legs_per_dog = 4
    total_legs = dogs * legs_per_dog
    result = total_legs
    return result

print(solution())