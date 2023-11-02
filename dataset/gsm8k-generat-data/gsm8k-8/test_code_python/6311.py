def solution():
    # Calculate the total cost of Thomas' order
    total_cost = 3*12 + 5 + 2*15 + 14

    # Check if the total cost is above $50.00
    if total_cost > 50:
        # Calculate the shipping cost as 20% of the total cost
        shipping_cost = 0.2 * total_cost
    else:
        # Otherwise, the shipping cost is a flat rate of $5.00
        shipping_cost = 5

    # Calculate the final bill by adding the total cost and the shipping cost
    final_bill = total_cost + shipping_cost
    result = final_bill
    return result

print(solution())