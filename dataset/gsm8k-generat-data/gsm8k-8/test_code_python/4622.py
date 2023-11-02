def solution():
    # Calculate the total cost of the televisions
    tv_cost = 5 * 50

    # Calculate the cost of the figurines
    figurine_cost = 260 - tv_cost

    # Calculate the cost of a single figurine
    single_figurine_cost = figurine_cost / 10
    result = single_figurine_cost
    return result

print(solution())