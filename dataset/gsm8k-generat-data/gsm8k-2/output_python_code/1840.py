def solution():
    """Mac loves the shape of quarters and is willing to trade money for them, even if he loses value. He tells his brother
    that he will trade him 3 dimes for a quarter or 7 nickels. He trades for 20 quarters with dimes and 20 quarters with
    nickels. How many dollars did Mac lose?"""
    # 3 dimes = 30 cents = 1 quarter, so 1 dime = 1/10 quarter
    # 7 nickels = 35 cents = 1 quarter, so 1 nickel = 1/7 quarter
    quarter_value = 0.25
    dime_value = 0.1
    nickel_value = 0.05
    dimes_per_quarter = 3
    nickels_per_quarter = 7
    total_quarters = 40
    quarters_with_dimes = 20
    quarters_with_nickels = 20
    total_dimes_used = quarters_with_dimes * dimes_per_quarter
    total_nickels_used = quarters_with_nickels * nickels_per_quarter
    total_value_paid = (total_dimes_used * dime_value) + (total_nickels_used * nickel_value)
    total_value_received = total_quarters * quarter_value
    total_loss = total_value_received - total_value_paid
    result = total_loss
    return result

print(solution())