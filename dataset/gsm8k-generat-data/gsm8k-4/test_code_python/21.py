def solution():
    """Each bird eats 12 beetles per day, each snake eats 3 birds per day, and each jaguar eats 5 snakes per day. If there are 6 jaguars in a forest, how many beetles are eaten each day?"""
    # Define the number of jaguars in the forest
    jaguars = 6

    # Calculate the number of snakes eaten per day by all jaguars
    snakes = jaguars * 5

    # Calculate the number of birds eaten per day by all snakes
    birds = snakes * 3

    # Calculate the number of beetles eaten per day by all birds
    beetles = birds * 12

    # return the result
    result = beetles
    return result

print(solution())