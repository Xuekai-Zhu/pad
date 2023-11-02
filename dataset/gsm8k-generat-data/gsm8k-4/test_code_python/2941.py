def solution():
    """Francine drives 140km to work each day. If she does not go to work 3 days every week, find the total distance she drives to work for 4 weeks in kilometers."""
    # Define the distance Francine drives to work each day
    distance_per_day = 140

    # Calculate the total distance Francine drives to work in a week
    distance_per_week = distance_per_day * (7 - 3)

    # Calculate the total distance Francine drives to work in 4 weeks
    total_distance = distance_per_week * 4

    # return the result
    result = total_distance
    return result

print(solution())