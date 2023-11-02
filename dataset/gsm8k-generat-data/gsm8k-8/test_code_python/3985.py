def solution():
    # Define the points scored by Lefty
    lefty_points = 20

    # Calculate the points scored by Righty
    righty_points = lefty_points / 2

    # Calculate the points scored by the other teammate
    other_teammate_points = righty_points * 6

    # Calculate the total points scored by the team
    total_points = lefty_points + righty_points + other_teammate_points

    # Calculate the average points scored per player
    average_points = total_points / 3

    result = average_points
    return result

print(solution())