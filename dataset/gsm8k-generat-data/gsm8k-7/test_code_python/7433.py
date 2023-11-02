def solution():
    console_price = 282
    initial_savings = 42
    weekly_allowance = 24

    # Calculate how much more money Woody needs to save
    remaining_money = console_price - initial_savings

    # Calculate how many weeks it will take Woody to save the remaining money
    num_weeks = remaining_money / weekly_allowance
    result = num_weeks
    return result

print(solution())