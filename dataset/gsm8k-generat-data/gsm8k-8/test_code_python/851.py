def solution():
    # Define the points for winning and the total points Jane had before losing
    win_points = 10
    total_points_before_loss = 60 + 20

    # Calculate the number of rounds Jane played
    num_rounds_played = total_points_before_loss // win_points
    result = num_rounds_played
    return result

print(solution())