def solution():
    toy_cost = 3  # Each toy costs $3
    num_toys = 5  # John buys 5 toys
    total_cost = toy_cost * num_toys  # The total cost before discount

    discount = 0.2  # John gets a 20% discount
    discount_amount = total_cost * discount  # Calculate the discount amount
    total_cost -= discount_amount  # Subtract the discount from the total cost

    result = total_cost
    return result

print(solution())