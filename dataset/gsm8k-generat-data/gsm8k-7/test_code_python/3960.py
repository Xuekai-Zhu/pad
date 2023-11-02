def solution():
    voltaire_viewers = 50
    leila_viewers = voltaire_viewers * 2
    earnings_per_view = 0.50
    num_days = 7

    # Calculate the total number of viewers Leila has in a week
    total_leila_viewers = leila_viewers * num_days

    # Calculate Leila's weekly earnings
    weekly_earnings = total_leila_viewers * earnings_per_view
    result = weekly_earnings
    return result

print(solution())