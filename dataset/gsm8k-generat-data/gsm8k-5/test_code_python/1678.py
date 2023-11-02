def solution():
    shampoo_cost = 10  # Cost of one bottle of shampoo
    conditioner_cost = 10  # Cost of one bottle of conditioner
    lotion_cost = 6  # Cost of one bottle of lotion
    lotion_quantity = 3  # Quantity of lotion bottles ordered
    required_spending = 50  # Amount required to be eligible for free shipping

    # Calculate the total cost of Jackie's order
    total_cost = shampoo_cost * 2 + conditioner_cost * 2 + lotion_cost * lotion_quantity

    # Calculate how much more money Jackie needs to spend to be eligible for free shipping
    additional_spending_required = required_spending - total_cost
    result = additional_spending_required
    return result

print(solution())