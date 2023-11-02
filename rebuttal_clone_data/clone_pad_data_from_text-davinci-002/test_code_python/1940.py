def solution():
    num_birds = 3
    num_dogs = 5
    num_snakes = 4
    num_spiders = 1
    total_legs = (num_birds * 2) + (num_dogs * 4) + (num_snakes * 0) + (num_spiders * 8)
    result = total_legs
    return result

print(solution())