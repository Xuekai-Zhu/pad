def solution():
    cost_of_iphone = 800  # The new iPhone costs $800
    trade_in_value = 240  # Carrie can trade in her old phone for $240
    money_from_babysitting = 80  # Carrie makes $80 per week babysitting

    # Calculate the total amount of money Carrie can save
    total_savings = trade_in_value

    # Calculate how many weeks it will take to save enough money to buy the iPhone
    weeks = 0
    while total_savings < cost_of_iphone:
        total_savings += money_from_babysitting
        weeks += 1

    result = weeks
    return result

print(solution())