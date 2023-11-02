def solution():
    # Calculate how much Alfonso can save each week
    weekly_savings = 6 * 5  # 6 dollars earn each day, walked 5 days a week

    # Calculate how much more money Alfonso needs to save
    remaining_cost = 340 - 40  # 340 dollars for the mountain bike helmet, already has 40 dollars

    # Calculate how many weeks Alfonso needs to work to save enough money
    num_weeks = remaining_cost / weekly_savings

    result = num_weeks
    return result

print(solution())