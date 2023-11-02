def solution():
    initial_tomatoes = 21
    birds_eat = (1/3) * initial_tomatoes
    remaining_tomatoes = initial_tomatoes - birds_eat
    result = remaining_tomatoes
    return result

print(solution())