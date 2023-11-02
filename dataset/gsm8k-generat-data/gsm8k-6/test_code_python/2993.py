def solution():
    # Calculate the total cost of John's order
    total_cost = 7 * 200  # each item costs $200
    discount_amount = 0
    if total_cost > 1000:
        discount_amount = (total_cost - 1000) * 0.10  # get 10% discount on the amount above $1000
        total_cost -= discount_amount
    
    result = total_cost
    return result

print(solution())