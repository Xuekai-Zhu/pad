def solution():
    """At the pet shop, there were 3 birds, 5 dogs, 4 snakes, and 1 spider for sale. How many legs were there in total?"""
    # Define the number of legs for each animal
    bird_legs = 2
    dog_legs = 4
    snake_legs = 0
    spider_legs = 8

    # Calculate the total number of legs
    total_legs = (3 * bird_legs) + (5 * dog_legs) + (4 * snake_legs) + (1 * spider_legs)

    # return the result
    result = total_legs
    return result

print(solution())