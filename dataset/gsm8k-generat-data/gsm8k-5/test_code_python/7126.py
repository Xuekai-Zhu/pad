def solution():
    washing_machine_cost = 100
    dryer_cost = washing_machine_cost - 30  # The dryer costs $30 less than the washing machine
    total_cost = washing_machine_cost + dryer_cost  # Calculate the total cost of the two appliances
    discount_amount = 0.1  # Hannah got a 10% discount
    discount = total_cost * discount_amount  # Calculate the discount amount
    discounted_total = total_cost - discount  # Calculate the total cost after the discount
    result = discounted_total
    return result

print(solution())