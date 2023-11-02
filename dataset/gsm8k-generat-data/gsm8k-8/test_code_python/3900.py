def solution():
    # Calculate the daily wage of one worker
    daily_wage_per_worker = 9450 / (15 * 6)

    # Calculate the total wage of 19 workers for 5 days
    total_wages = daily_wage_per_worker * (19 * 5)

    result = total_wages
    return result

print(solution())