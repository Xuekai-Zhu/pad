def solution():
    """Ellen is baking bread. It takes 3 hours to rise 1 ball of dough, and then another 2 hours to bake it. If she makes 4 balls of dough one after another and then bakes them one after another when they're done rising, how many hours will it take?"""
    # Define the time it takes to rise and bake one ball of dough
    RISE_TIME = 3
    BAKE_TIME = 2

    # Define the number of balls of dough
    num_dough = 4

    # Calculate the total time it takes to rise all balls of dough
    rise_total = RISE_TIME * num_dough

    # Calculate the total time it takes to bake all balls of dough
    bake_total = BAKE_TIME * num_dough

    # Calculate the total time
    total_time = rise_total + bake_total

    # Return the result
    result = total_time
    return result

print(solution())