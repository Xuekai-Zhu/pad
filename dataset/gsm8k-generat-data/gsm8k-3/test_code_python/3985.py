def solution():
    """Lefty scores 20 points in a game and his teammate Righty scores half as many as Lefty does.  Their other teammate scores 6 times as much as Righty does.  What are the average points scored per player on the team?"""
    # Calculate the number of points scored by Righty
    righty_points = 20 / 2

    # Calculate the number of points scored by the third teammate
    third_teammate_points = righty_points * 6

    # Calculate the total points scored by the team
    total_points = 20 + righty_points + third_teammate_points

    # Calculate the average points per player
    average_points = total_points / 3

    # Display the average points per player
    result = average_points
    return result

print(solution())