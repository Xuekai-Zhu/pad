def solution():
    # Calculate the total number of legs of all the animals for sale
    bird_legs = 2  # each bird has 2 legs
    dog_legs = 4  # each dog has 4 legs
    snake_legs = 0  # snakes don't have legs
    spider_legs = 8  # each spider has 8 legs
    total_legs = 3*bird_legs + 5*dog_legs + 4*snake_legs + 1*spider_legs
    result = total_legs
    return result

print(solution())