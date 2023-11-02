def solution():
    distance_per_day = 140  # Francine drives 140 km to work each day
    days_per_week = 5  # Francine works 5 days per week
    weeks = 4  # Francine wants to know the total distance she drives to work for 4 weeks

    # Calculate the total distance Francine drives to work in 4 weeks
    total_distance = distance_per_day * days_per_week * weeks

    # Subtract the distance for the 3 days Francine does not go to work each week
    total_distance -= distance_per_day * 3 * weeks

    result = total_distance
    return result

print(solution())