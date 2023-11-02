def solution():
    # Define the number of toys and their individual cost
    num_toys = 5
    toy_cost = 3

    # Calculate the total cost before discount
    total_cost = num_toys * toy_cost

    # Apply the discount
    discount_percent = 20
    discount_amount = total_cost * (discount_percent/100)
    discounted_total = total_cost - discount_amount

    result = discounted_total
    return result

print(solution())