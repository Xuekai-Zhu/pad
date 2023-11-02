def solution():
    # Define Bill's daily toilet paper usage
    daily_usage = 3 * 5

    # Calculate the total toilet paper usage for the entire supply
    total_usage = daily_usage * 1000 * 300

    # Calculate the number of days the supply will last
    days_supply = total_usage // daily_usage
    result = days_supply
    return result

print(solution())