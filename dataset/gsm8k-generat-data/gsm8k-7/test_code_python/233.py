def solution():
    sets = 3
    reps_per_set = 15

    # Calculate the total number of push-ups expected
    expected_pushups = sets * reps_per_set

    # Calculate the number of push-ups Bryan did in the last set
    actual_last_set = reps_per_set - 5

    # Calculate the total number of push-ups Bryan did
    total_pushups = (sets - 1) * reps_per_set + actual_last_set

    result = total_pushups
    return result

print(solution())