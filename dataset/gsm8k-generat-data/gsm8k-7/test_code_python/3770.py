def solution():
    num_soccer_balls = 40
    num_basketballs = 15
    num_holes_soccer = 30
    num_holes_basketball = 7

    # Calculate the number of soccer balls without holes
    num_soccer_no_holes = num_soccer_balls - num_holes_soccer

    # Calculate the number of basketballs without holes
    num_basketball_no_holes = num_basketballs - num_holes_basketball

    # Calculate the total number of balls without holes
    total_no_holes = num_soccer_no_holes + num_basketball_no_holes
    result = total_no_holes
    return result

print(solution())