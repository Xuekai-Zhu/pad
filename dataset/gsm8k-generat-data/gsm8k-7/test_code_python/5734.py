def solution():
    full_ladder_steps = 11
    full_ladder_freq = 10
    small_ladder_steps = 6
    small_ladder_freq = 7

    # Calculate the total number of steps Darry climbed on his full ladder
    full_ladder_total_steps = full_ladder_steps * full_ladder_freq

    # Calculate the total number of steps Darry climbed on his small ladder
    small_ladder_total_steps = small_ladder_steps * small_ladder_freq

    # Calculate the total number of steps Darry climbed today
    total_steps = full_ladder_total_steps + small_ladder_total_steps
    result = total_steps
    return result

print(solution())