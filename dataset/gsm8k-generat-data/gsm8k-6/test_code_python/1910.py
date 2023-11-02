def solution():
    # Calculate Johnson's yield per 2-month period
    johnson_yield = 80

    # Calculate neighbor's yield per 2-month period
    neighbor_yield = 2 * (2 * johnson_yield)

    # Calculate total yield for 6 months
    total_yield = (johnson_yield * 3) + (neighbor_yield * 3)

    result = total_yield
    return result

print(solution())