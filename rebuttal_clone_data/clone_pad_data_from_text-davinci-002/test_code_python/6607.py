def solution():
    total_nails = 164
    nails_per_dog = 4
    nails_per_leg = nails_per_dog / 3
    total_dogs = total_nails / nails_per_leg
    result = total_dogs
    return result

print(solution())