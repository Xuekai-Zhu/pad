def solution():
    # Calculate the number of snakes eaten by all jaguars in one day
    snakes_eaten = 6 * 5 * 3

    # Calculate the number of beetles eaten by all snakes in one day
    beetles_eaten = snakes_eaten * 12

    result = beetles_eaten
    return result

print(solution())