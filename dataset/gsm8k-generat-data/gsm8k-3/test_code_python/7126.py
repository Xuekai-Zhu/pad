def solution():
    """Hannah bought a new washing machine for $100 and a dryer that costs $30 less. Hannah got a 10% discount for buying two appliances. How much did Hannah pay for the two appliances after the discount?"""
    # Define the cost of the washing machine and the dryer
    washing_machine_cost = 100
    dryer_cost = washing_machine_cost - 30

    # Calculate the total cost before discount
    total_cost_before_discount = washing_machine_cost + dryer_cost

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * 0.1

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # Display the total cost after discount
    result = total_cost_after_discount
    return result

print(solution())