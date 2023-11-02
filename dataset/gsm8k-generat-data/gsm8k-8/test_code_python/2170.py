def solution():
    # Define the cost of one set of barrettes and one comb
    barrettes_cost = 3
    comb_cost = 1

    # Calculate Kristine's total cost
    kristine_cost = barrettes_cost + comb_cost

    # Calculate Crystal's total cost
    crystal_cost = 3 * barrettes_cost + comb_cost

    # Calculate the total cost for both girls
    total_cost = kristine_cost + crystal_cost

    result = total_cost
    return result

print(solution())