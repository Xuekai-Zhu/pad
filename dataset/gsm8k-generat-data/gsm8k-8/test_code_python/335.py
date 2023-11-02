def solution():
    # Define the cost of each item
    mitt_cost = 14
    apron_cost = 16
    utensil_cost = 10
    knife_cost = 2 * utensil_cost

    # Calculate the total cost before the discount
    total_cost = 3 * (mitt_cost + apron_cost + utensil_cost + knife_cost)

    # Calculate the discount amount
    discount_amount = 0.25 * total_cost

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost - discount_amount
    result = total_cost_after_discount
    return result

print(solution())