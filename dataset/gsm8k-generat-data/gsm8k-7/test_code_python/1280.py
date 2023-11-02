def solution():
    daily_earnings = 80
    num_days = 20
    total_spent = 1360

    # Calculate the total earnings for 20 days
    total_earnings = daily_earnings * num_days

    # Calculate the total amount saved in 20 days
    total_saved = total_earnings - total_spent
    result = total_saved
    return result

print(solution())