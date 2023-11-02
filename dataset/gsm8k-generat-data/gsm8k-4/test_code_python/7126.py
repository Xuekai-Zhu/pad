def solution():
    """Hannah bought a new washing machine for $100 and a dryer that costs $30 less. Hannah got a 10% discount for buying two appliances. How much did Hannah pay for the two appliances after the discount?"""
    # Define the original prices of the washing machine and dryer
    washing_machine_price = 100
    dryer_price = washing_machine_price - 30

    # Calculate the total before the discount
    total_before_discount = washing_machine_price + dryer_price

    # Calculate the discount amount
    discount = total_before_discount * 0.1

    # Calculate the total after the discount
    total_after_discount = total_before_discount - discount

    result = total_after_discount
    return result

print(solution())