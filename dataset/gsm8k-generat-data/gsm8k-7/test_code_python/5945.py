def solution():
    num_folds = 4
    time_per_fold = 5
    rest_time = 75
    mixing_time = 10
    baking_time = 30

    # Calculate the total time for folding the dough
    total_folding_time = num_folds * time_per_fold

    # Calculate the total time for letting the dough rest
    total_rest_time = num_folds * rest_time

    # Calculate the total time for the whole process in minutes
    total_time = total_folding_time + total_rest_time + mixing_time + baking_time

    # Convert the total time to hours
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())