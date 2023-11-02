def solution():
    # Calculate the total cost of candy bars, chocolate, and juice
    total_cost = (3 * 25) + (2 * 75) + 50

    # Calculate the number of quarters needed to pay the total cost
    num_quarters = total_cost // 25
    result = num_quarters
    return result

print(solution())