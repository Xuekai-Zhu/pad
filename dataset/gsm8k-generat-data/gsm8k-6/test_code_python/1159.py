def solution():
    # Calculate the cost of the shoes after the 30% discount
    cost_shoes = 200 * (1 - 0.3)

    # Calculate the total cost of the shirts
    cost_shirts = 2 * 80

    # Calculate the total cost before the additional 5% discount
    total_cost = cost_shoes + cost_shirts

    # Calculate the cost after the additional 5% discount
    final_cost = total_cost * (1 - 0.05)
    result = final_cost
    return result

print(solution())