def solution():
    bottles_per_year = 12
    cost_per_bottle = 30.0
    discount = 0.3  # 30% discount

    # Calculate the total cost of all bottles without the discount
    total_cost = bottles_per_year * cost_per_bottle

    # Calculate the discount amount
    discount_amount = total_cost * discount

    # Calculate the total cost of all bottles with the discount
    total_cost_with_discount = total_cost - discount_amount
    result = total_cost_with_discount
    return result

print(solution())