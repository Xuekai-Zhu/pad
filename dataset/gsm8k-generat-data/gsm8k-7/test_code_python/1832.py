def solution():
    total_balls = 145
    num_soccer_balls = 20
    num_basketballs = num_soccer_balls + 5
    num_tennis_balls = 2 * num_soccer_balls
    num_baseballs = num_soccer_balls + 10

    # Calculate the total number of other balls besides soccer balls
    total_other_balls = num_basketballs + num_tennis_balls + num_baseballs

    # Calculate the number of volleyball balls
    num_volleyballs = total_balls - num_soccer_balls - total_other_balls
    result = num_volleyballs
    return result

print(solution())