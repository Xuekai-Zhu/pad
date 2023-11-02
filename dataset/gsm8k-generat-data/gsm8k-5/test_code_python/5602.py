def solution():
    initial_cats = 28
    initial_dogs = 18
    cats_given_away = 3
    cats_remaining = initial_cats - cats_given_away
    dogs_remaining = initial_dogs
    cats_more_than_dogs = cats_remaining - dogs_remaining
    result = cats_more_than_dogs
    return result

print(solution())