def solution():
    # Calculate how much money Alfonso earns each week
    weekly_income = 6 * 5  # Alfonso walks the dog 5 days a week

    # Calculate how much money Alfonso needs to save
    total_cost = 340 - 40  # Alfonso already has $40

    # Calculate how many weeks Alfonso needs to work to reach his savings goal
    weeks_to_save = total_cost / weekly_income

    result = weeks_to_save
    return result

print(solution())