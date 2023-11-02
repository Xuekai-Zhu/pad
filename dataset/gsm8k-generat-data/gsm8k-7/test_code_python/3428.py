def solution():
    num_tickets = 24
    original_price = 7
    discount = 0.5  # 50% discount

    # Calculate the total cost without the discount
    original_cost = num_tickets * original_price

    # Calculate the total discount
    total_discount = original_cost * discount

    # Calculate the total cost with the discount
    total_cost = original_cost - total_discount
    result = total_cost
    return result

print(solution())