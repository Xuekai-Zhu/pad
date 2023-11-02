def solution():
    """Francine drives 140km to work each day. If she does not go to work 3 days every week, find the total distance she drives to work for 4 weeks in kilometers."""
    # Define the distance Francine drives to work each week
    weekly_distance = 140 * (7 - 3) # Francine doesn't go to work 3 days every week

    # Calculate the total distance Francine drives to work for 4 weeks
    total_distance = weekly_distance * 4

    # Display the total distance
    result = total_distance
    return result

print(solution())