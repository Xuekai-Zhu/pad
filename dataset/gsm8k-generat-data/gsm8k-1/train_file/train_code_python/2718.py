def solution():
    """Ellen is baking bread. It takes 3 hours to rise 1 ball of dough, and then another 2 hours to bake it. If she makes 4 balls of dough one after another and then bakes them one after another when they’re done rising, how many hours will it take?"""
    rise_time = 3
    bake_time = 2
    num_balls = 4
    total_time = (rise_time + bake_time) * num_balls
    result = total_time
    return result

print(solution())