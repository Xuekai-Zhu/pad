def solution():
    """At the pet shop, there were 3 birds, 5 dogs, 4 snakes, and 1 spider for sale. How many legs were there in total?"""
    # Define the number of legs for each type of animal
    BIRD_LEGS = 2
    DOG_LEGS = 4
    SNAKE_LEGS = 0
    SPIDER_LEGS = 8

    # Define the number of each type of animal
    num_birds = 3
    num_dogs = 5
    num_snakes = 4
    num_spiders = 1

    # Calculate the total number of legs
    total_legs = num_birds * BIRD_LEGS + num_dogs * DOG_LEGS + num_snakes * SNAKE_LEGS + num_spiders * SPIDER_LEGS

    # Display the total number of legs
    result = total_legs
    return result

print(solution())