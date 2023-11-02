def solution():
    """Each bird eats 12 beetles per day, each snake eats 3 birds per day, and each jaguar eats 5 snakes per day. If there are 6 jaguars in a forest, how many beetles are eaten each day?"""
    bird_eats = 12
    snake_eats = 3 * bird_eats
    jaguar_eats = 5 * snake_eats
    total_beetles_eaten = jaguar_eats * 6
    result = total_beetles_eaten
    return result

print(solution())