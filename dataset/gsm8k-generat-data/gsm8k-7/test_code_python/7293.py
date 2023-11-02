def solution():
    total_animals = 21
    num_dogs = 2*num_cats

    # We know that the total number of animals spayed is 21, so we can solve for num_cats
    num_cats = (total_animals)/(2+1)

    result = num_cats
    return result

print(solution())