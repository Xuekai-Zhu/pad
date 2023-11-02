def solution():
    # Define the number of legs each animal type has
    bird_legs = 2
    dog_legs = 4
    snake_legs = 0
    spider_legs = 8

    # Calculate the total number of legs
    total_legs = (3 * bird_legs) + (5 * dog_legs) + (4 * snake_legs) + (1 * spider_legs)
    result = total_legs
    return result

print(solution())