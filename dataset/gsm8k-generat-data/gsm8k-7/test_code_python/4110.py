def solution():
    suit_cost = 430
    shoes_cost = 190
    discount = 100

    # Calculate the total cost before the discount
    total_cost = suit_cost + shoes_cost

    # Calculate the total cost after the discount
    total_cost -= discount

    result = total_cost
    return result

print(solution())