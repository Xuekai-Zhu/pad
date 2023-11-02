def solution():
    cows = 184
    dogs = cows / 2
    cows_sold = cows / 4
    dogs_sold = dogs * 3 / 4
    remaining_cows = cows - cows_sold
    remaining_dogs = dogs - dogs_sold
    remaining_animals = remaining_cows + remaining_dogs
    result = remaining_animals
    return result

print(solution())