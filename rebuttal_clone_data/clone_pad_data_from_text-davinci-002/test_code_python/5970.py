def solution():
    pieces_per_serving = 30
    Jared_can_eat = 90
    friends_can_eat = 60
    servings_needed = Jared_can_eat / pieces_per_serving + friends_can_eat / pieces_per_serving
    result = servings_needed
    return result

print(solution())