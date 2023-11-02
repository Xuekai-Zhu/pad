def solution():
    # Calculate the total amount of money Vanessa can save each week
    weekly_savings = 30 - 10  # Vanessa gets $30 every week, but spends $10 on arcades

    # Calculate how many weeks Vanessa will have to wait to save enough money
    weeks_needed = (80 - 20) / weekly_savings
    result = weeks_needed
    return result

print(solution())