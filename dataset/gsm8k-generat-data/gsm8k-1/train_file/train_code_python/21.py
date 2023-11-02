def solution():
    """Each bird eats 12 beetles per day, each snake eats 3 birds per day, and each jaguar eats 5 snakes per day. If there are 6 jaguars in a forest, how many beetles are eaten each day?"""
    beetles_per_bird = 12
    birds_per_snake = 3
    snakes_per_jaguar = 5
    jaguars_in_forest = 6
    snakes_eaten_per_day = jaguars_in_forest * snakes_per_jaguar
    birds_eaten_per_day = snakes_eaten_per_day * birds_per_snake
    beetles_eaten_per_day = birds_eaten_per_day * beetles_per_bird
    result = beetles_eaten_per_day
    return result

print(solution())