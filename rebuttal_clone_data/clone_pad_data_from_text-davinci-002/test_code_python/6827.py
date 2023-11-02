def solution():
    initial_cranberries = 60000
    cranberries_harvested = initial_cranberries * 0.40
    cranberries_eaten = 20000
    cranberries_left = initial_cranberries - cranberries_harvested - cranberries_eaten
    result = cranberries_left
    return result

print(solution())