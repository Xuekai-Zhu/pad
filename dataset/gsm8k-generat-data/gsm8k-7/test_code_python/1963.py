def solution():
    total_sales = 24000
    commission_rate = 0.12
    personal_needs_percentage = 0.6

    # Calculate the total commission Christine earned
    total_commission = total_sales * commission_rate

    # Calculate the amount of money allocated to Christine's personal needs
    personal_needs = total_commission * personal_needs_percentage

    # Calculate the amount of money saved by Christine
    saved_money = total_commission - personal_needs
    result = saved_money
    return result

print(solution())