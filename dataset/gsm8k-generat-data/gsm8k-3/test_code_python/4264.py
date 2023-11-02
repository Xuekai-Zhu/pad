def solution():
    """Marcus scored 5 3-point goals and 10 2-point goals. If his team scored 70 points overall, what percentage of the team's total points did Marcus score?"""
    # Calculate the total points Marcus scored
    total_points = 5*3 + 10*2

    # Calculate the percentage of the team's total points that Marcus scored
    percentage = (total_points/70)*100

    # Display the percentage
    result = percentage
    return result

print(solution())