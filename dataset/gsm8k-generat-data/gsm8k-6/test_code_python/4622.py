def solution():
    # Calculate the cost of the 5 televisions
    tv_cost = 5 * 50  

    # Calculate the total cost of the purchase
    total_cost = tv_cost + 10 * x  # x is the cost of a single figurine

    # Calculate the cost of a single figurine
    x = (260 - tv_cost) / 10 

    result = x
    return result

print(solution())