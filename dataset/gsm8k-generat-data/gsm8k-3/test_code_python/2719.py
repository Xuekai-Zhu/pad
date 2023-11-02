def solution():
    """Ellen is baking bread. It takes 3 hours to rise 1 ball of dough, and then another 2 hours to bake it. If she makes 4 balls of dough one after another and then bakes them one after another when they're done rising, how many hours will it take?"""
    # Define the time it takes to rise one ball of dough and bake it
    RISE_TIME = 3
    BAKE_TIME = 2

    # Define the number of balls of dough Ellen makes
    balls_of_dough = 4

    # Calculate the total time it takes to rise all the balls of dough
    rise_time = RISE_TIME * balls_of_dough

    # Calculate the total time it takes to bake all the balls of dough
    bake_time = BAKE_TIME * balls_of_dough

    # Calculate the total time it takes to make and bake all the balls of dough
    total_time = rise_time + bake_time

    # Display the total time
    result = total_time
    return result

print(solution())