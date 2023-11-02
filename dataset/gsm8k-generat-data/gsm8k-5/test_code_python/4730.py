def solution():
    # Calculate the number of dogs at the petting farm
    cows = 184
    dog_cows_ratio = 1/2
    dogs = cows / dog_cows_ratio

    # Calculate the number of animals remaining after selling 1/4 of cows and 3/4 of dogs
    cows_remaining = round(cows * 0.75)
    dogs_remaining = round(dogs * 0.25)
    total_remaining = cows_remaining + dogs_remaining

    result = total_remaining
    return result

print(solution())