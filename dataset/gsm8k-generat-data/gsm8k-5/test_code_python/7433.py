def solution():
    console_cost = 282  # The cost of the games console
    woody_savings = 42  # Woody already has $42
    weekly_allowance = 24  # Woody gets $24 allowance every week

    # Calculate the amount of money Woody needs to save
    money_needed = console_cost - woody_savings

    # Calculate the number of weeks Woody needs to save
    weeks_needed = money_needed / weekly_allowance
    result = weeks_needed
    return result

print(solution())