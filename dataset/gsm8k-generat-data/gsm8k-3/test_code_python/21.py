def solution():
    """Each bird eats 12 beetles per day, each snake eats 3 birds per day, and each jaguar eats 5 snakes per day. If there are 6 jaguars in a forest, how many beetles are eaten each day?"""
    # Define the number of jaguars
    num_jaguars = 6

    # Calculate the number of snakes eaten each day by all jaguars
    num_snakes = num_jaguars * 5

    # Calculate the number of birds eaten each day by all snakes
    num_birds = num_snakes * 3

    # Calculate the number of beetles eaten each day by all birds
    num_beetles = num_birds * 12

    # return the result
    result = num_beetles
    return result

print(solution())