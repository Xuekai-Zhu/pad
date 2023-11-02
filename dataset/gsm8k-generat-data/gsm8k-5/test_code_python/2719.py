def solution():
    time_to_rise = 3  # It takes 3 hours to rise 1 ball of dough
    time_to_bake = 2  # It takes 2 hours to bake 1 ball of dough
    num_balls = 4  # Ellen is making 4 balls of dough

    # Calculate the total time to rise all 4 balls of dough
    total_rise_time = num_balls * time_to_rise

    # Calculate the total time to bake all 4 balls of dough
    total_bake_time = num_balls * time_to_bake

    # Calculate the total time it will take to make and bake all 4 balls of dough
    total_time = total_rise_time + total_bake_time
    result = total_time
    return result

print(solution())