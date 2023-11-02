def solution():
    """Marcus scored 5 3-point goals and 10 2-point goals. If his team scored 70 points overall, what percentage of the team's total points did Marcus score?"""
    # Define the points for a 3-point goal and a 2-point goal
    THREE_POINT_GOAL = 3
    TWO_POINT_GOAL = 2

    # Calculate Marcus's total points
    marcus_points = (5 * THREE_POINT_GOAL) + (10 * TWO_POINT_GOAL)

    # Calculate the percentage of the team's total points that Marcus scored
    total_points = 70
    marcus_percentage = (marcus_points / total_points) * 100

    # return the result
    result = marcus_percentage
    return result

print(solution())