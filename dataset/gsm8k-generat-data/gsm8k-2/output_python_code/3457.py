def solution():
    """Jake delivers 234 newspapers a week. Miranda delivers twice as many newspapers a week. How many more newspapers does Miranda deliver than Jake in a month?"""
    jake_weekly_newspapers = 234
    miranda_weekly_newspapers = 2 * jake_weekly_newspapers
    monthly_newspapers_difference = (miranda_weekly_newspapers - jake_weekly_newspapers) * 4
    result = monthly_newspapers_difference
    return result

print(solution())