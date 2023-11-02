def solution():
    # Define the number of legs per animal
    bird_legs = 2
    dog_legs = 4
    snake_legs = 0
    spider_legs = 8

    # Define the number of each type of animal for sale
    num_birds = 3
    num_dogs = 5
    num_snakes = 4
    num_spiders = 1

    # Calculate the total number of legs for all animals
    total_legs = (num_birds * bird_legs) + (num_dogs * dog_legs) + (num_snakes * snake_legs) + (num_spiders * spider_legs)
    result = total_legs
    return result

print(solution())