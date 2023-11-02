def solution():
    voltaire_avg_viewers = 50
    leila_avg_viewers = 2 * voltaire_avg_viewers

    # Calculate the total earnings of Voltaire and Leila per day
    voltaire_day_earnings = voltaire_avg_viewers * 0.5
    leila_day_earnings = leila_avg_viewers * 0.5

    # Calculate the total earnings of Leila per week
    leila_weekly_earnings = leila_day_earnings * 7
    result = leila_weekly_earnings
    return result

print(solution())