def solution():
    time_to_rise = 3  # hours
    time_to_bake = 2  # hours
    num_balls_of_dough = 4

    # Calculate the total time it takes for all balls of dough to rise
    total_rise_time = time_to_rise * num_balls_of_dough

    # Calculate the total time it takes to bake all balls of dough
    total_bake_time = time_to_bake * num_balls_of_dough

    # Calculate the total time it takes for all balls of dough to be ready
    total_time = total_rise_time + total_bake_time
    result = total_time
    return result

print(solution())