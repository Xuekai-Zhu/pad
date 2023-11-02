def solution():
    # Calculate the points earned from the wins
    win_points = 14 * 3

    # Calculate the points earned from the draws
    draw_points = (20 - 14 - 2) * 1

    # Calculate the total points earned
    total_points = win_points + draw_points
    result = total_points
    return result

print(solution())