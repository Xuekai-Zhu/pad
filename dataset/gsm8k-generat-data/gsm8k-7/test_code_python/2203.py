def solution():
    initial_eggs = 20
    morning_eggs = 4
    afternoon_eggs = 3

    # Calculate the total number of eggs Ben ate
    total_eggs_eaten = morning_eggs + afternoon_eggs

    # Calculate the number of eggs Ben has left
    eggs_left = initial_eggs - total_eggs_eaten
    result = eggs_left
    return result

print(solution())