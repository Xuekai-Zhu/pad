def solution():
    old_system_cost = 250
    trade_in_value_percent = 0.8
    new_system_cost = 600
    discount_percent = 0.25

    # Calculate the trade-in value of the old system
    trade_in_value = old_system_cost * trade_in_value_percent

    # Calculate the discounted price of the new system
    discounted_price = new_system_cost * (1 - discount_percent)

    # Calculate the total amount of money out of pocket
    money_out_of_pocket = discounted_price - trade_in_value
    result = money_out_of_pocket
    return result

print(solution())