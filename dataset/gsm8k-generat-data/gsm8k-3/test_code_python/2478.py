def solution():
    """In a game, Samanta has 8 more points than Mark, and Mark has 50% more points than Eric. Eric has 6 points. How many points do Samanta, Mark, and Eric have in total?"""
    # Define the number of points Eric has
    eric_points = 6

    # Calculate the number of points Mark has
    mark_points = eric_points * 1.5

    # Calculate the number of points Samanta has
    samanta_points = mark_points + 8

    # Calculate the total number of points
    total_points = eric_points + mark_points + samanta_points

    # Display the total number of points
    result = total_points
    return result

print(solution())