def solution():
    """Jamie is in a walking group with 4 other ladies. The ladies all walk 3 miles together. On top of that, Jamie walks an additional 2 miles per day for 6 days while her friend Sue walks half that amount in 6 days. If they walk this same route 6 days a week, how many miles do the ladies walk in total?"""
    # Define the initial group walking distance and the number of days
    GROUP_WALKING_DISTANCE = 3
    NUM_DAYS = 6

    # Define Jamie's additional walking distance and Sue's walking distance
    JAMIE_ADDITIONAL_DISTANCE = 2
    SUE_DISTANCE = JAMIE_ADDITIONAL_DISTANCE / 2

    # Calculate the total group walking distance
    group_total_distance = GROUP_WALKING_DISTANCE * NUM_DAYS

    # Calculate Jamie's total walking distance
    jamie_total_distance = JAMIE_ADDITIONAL_DISTANCE * NUM_DAYS + group_total_distance

    # Calculate Sue's total walking distance
    sue_total_distance = SUE_DISTANCE * NUM_DAYS + group_total_distance

    # Calculate the total walking distance for the group
    group_total_distance = group_total_distance * 5 + jamie_total_distance + sue_total_distance

    # Return the result
    result = group_total_distance
    return result

print(solution())