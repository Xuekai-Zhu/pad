def solution():
    # Calculate the cost of pool cleaning per month
    pool_cleaning_cost = 150 * (30 / 3) * 1.1

    # Calculate the cost of pool chemicals per month
    pool_chemicals_cost = 200 * 2

    # Calculate the total monthly cost of the pool
    total_cost = pool_cleaning_cost + pool_chemicals_cost

    result = total_cost
    return result

print(solution())