def solution():
    allowance_prev = 5
    weeks_prev = 8
    allowance_new = 6
    weeks_new = 6
    clothes_ratio = 0.5
    game_cost = 35

    # Calculate total allowance from previous weeks
    total_allowance_prev = allowance_prev * weeks_prev

    # Calculate total allowance from new weeks
    total_allowance_new = allowance_new * weeks_new

    # Calculate total allowance Francie saved up
    total_allowance = total_allowance_prev + total_allowance_new

    # Calculate how much Francie spent on clothes
    clothes_cost = total_allowance * clothes_ratio

    # Calculate how much Francie has left after buying the video game
    left_over_money = total_allowance - clothes_cost - game_cost
    result = left_over_money
    return result

print(solution())