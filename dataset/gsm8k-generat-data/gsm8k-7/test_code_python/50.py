def solution():
    baseball_spending = 100
    season_length = 4
    savings_goal = baseball_spending * season_length
    non_season_months = 12 - season_length
    earnings_per_chore = 10

    # Calculate how much Gerald needs to save each non-season month
    savings_per_month = savings_goal / non_season_months

    # Calculate how many chores Gerald needs to do each non-season month to reach his savings goal
    chores_per_month = savings_per_month / earnings_per_chore
    result = chores_per_month
    return result

print(solution())