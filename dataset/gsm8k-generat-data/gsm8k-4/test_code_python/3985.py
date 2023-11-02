def solution():
    """Lefty scores 20 points in a game and his teammate Righty scores half as many as Lefty does. Their other teammate scores 6 times as much as Righty does. What are the average points scored per player on the team?"""
    # Define the number of points scored by Lefty and calculate the number of points scored by Righty
    lefty_points = 20
    righty_points = lefty_points / 2

    # Calculate the number of points scored by the other teammate
    other_teammate_points = righty_points * 6

    # Calculate the total number of points scored by the team
    total_points = lefty_points + righty_points + other_teammate_points

    # Calculate the average number of points scored per player
    average_points = total_points / 3

    # Return the result
    result = average_points
    return result

print(solution())