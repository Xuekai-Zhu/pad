def solution():
    # Calculate the time required to fold the dough
    time_folding = 4 * 5  # 4 folds, each taking 5 minutes

    # Calculate the time required for the dough to rest
    time_resting = 4 * 75  # 4 rest periods, each taking 75 minutes

    # Calculate the total time required for the dough preparation
    time_preparation = time_folding + time_resting + 10  # 10 minutes for mixing the ingredients

    # Calculate the total time required for the whole process, including baking
    time_total = time_preparation + 30  # 30 minutes for baking

    # Convert the time to hours
    hours_total = time_total / 60

    result = hours_total
    return result

print(solution())