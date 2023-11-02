def solution():
    # Calculate the trade-in value and cost of new system after discount
    trade_in_value = 250 * 0.8  # John gets 80% of the value for his old system
    new_system_cost = 600 * 0.75  # John gets a 25% discount on the new system

    # Calculate the amount of money John paid out of pocket
    out_of_pocket = new_system_cost - trade_in_value
    result = out_of_pocket
    return result

print(solution())