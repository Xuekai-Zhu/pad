def solution():
    # Calculate the total time needed to fold the dough and let it rest
    time_folding_dough = 4 * 5  # 4 folds that take 5 minutes each
    time_resting_dough = 4 * 75  # 75 minutes of resting time after each fold
    total_time_dough = time_folding_dough + time_resting_dough

    # Calculate the total time needed for mixing and baking
    time_mixing = 10
    time_baking = 30
    total_time_baking = time_mixing + time_baking

    # Calculate the total time for the whole process in hours
    total_time = (total_time_dough + total_time_baking) / 60  # convert to hours
    result = total_time
    return result

print(solution())