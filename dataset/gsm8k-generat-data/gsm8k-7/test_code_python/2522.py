def solution():
    large_cost = 15
    total_cost = 23
    num_small = 3

    # Calculate the cost of the small puzzle
    small_cost = total_cost - large_cost

    # Calculate the cost of 3 small puzzles and 1 large puzzle
    total_payment = (3 * small_cost) + large_cost
    result = total_payment
    return result

print(solution())