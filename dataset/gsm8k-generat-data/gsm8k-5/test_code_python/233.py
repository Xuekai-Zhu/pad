def solution():
    # Calculate the total number of push-ups Bryan did in the first two sets
    first_two_sets = 2 * 15  # 2 sets of 15 push-ups each

    # Calculate the number of push-ups Bryan did in the third set
    third_set = 15 - 5  # Bryan did 5 fewer push-ups in the third set

    # Calculate the total number of push-ups Bryan did
    total_pushups = first_two_sets + third_set
    result = total_pushups
    return result

print(solution())