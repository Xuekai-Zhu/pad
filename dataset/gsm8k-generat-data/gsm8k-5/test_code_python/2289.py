def solution():
    # Calculate the cost of the first two books after the 25% discount
    discounted_cost = 0.75 * (13 + 15)

    # Calculate the total cost of all 4 books
    total_cost = discounted_cost + 2*10

    # Check if the total cost is greater than $50. If so, no additional spending is needed for free shipping
    if total_cost >= 50:
        return 0

    # Calculate the additional amount needed to reach $50
    additional_cost_needed = 50 - total_cost
    result = additional_cost_needed
    return result

print(solution())