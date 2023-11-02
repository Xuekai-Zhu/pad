def solution():
    # Calculate Lisa's spending
    tshirt_cost = 40
    jeans_cost = tshirt_cost/2
    coats_cost = 2*tshirt_cost
    lisa_spending = tshirt_cost + jeans_cost + coats_cost

    # Calculate Carly's spending
    carly_tshirt_cost = tshirt_cost/4
    carly_jeans_cost = 3*jeans_cost
    carly_coats_cost = coats_cost/4
    carly_spending = carly_tshirt_cost + carly_jeans_cost + carly_coats_cost

    # Calculate total spending
    total_spending = lisa_spending + carly_spending
    result = total_spending
    return result

print(solution())