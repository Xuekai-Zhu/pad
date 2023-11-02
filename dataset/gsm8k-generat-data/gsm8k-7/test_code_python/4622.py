def solution():
    num_TVs = 5
    TV_price = 50

    total_cost = 260

    # Calculate the total cost of all TVs
    total_TV_cost = num_TVs * TV_price

    # Calculate the cost of all figurines
    figurine_cost = total_cost - total_TV_cost

    # Calculate the cost of a single figurine
    cost_per_figurine = figurine_cost / 10
    result = cost_per_figurine
    return result

print(solution())