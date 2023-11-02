def solution():
    
    cows = 184
    dogs = cows / 2
    sold_cows = cows / 4
    sold_dogs = dogs * 3 / 4
    remaining_cows = cows - sold_cows
    remaining_dogs = dogs - sold_dogs
    total_animals = remaining_cows + remaining_dogs
    result = total_animals
    return result

print(solution())