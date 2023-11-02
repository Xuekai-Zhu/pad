def solution():
    initial_wins = 10
    first_streak = 5
    second_streak = first_streak * 2
    losses = 2

    # Calculate the total number of wins
    total_wins = initial_wins + first_streak + second_streak

    # Calculate the total number of losses
    total_losses = losses

    # Calculate the difference between wins and losses
    difference = total_wins - total_losses
    result = difference
    return result

print(solution())