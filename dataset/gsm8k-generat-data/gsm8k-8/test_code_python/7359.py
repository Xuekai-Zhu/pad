def solution():
    # Calculate the total cost of the items excluding the coats and the shoes
    total_excl_coats_shoes = 110 - 40 - 30

    # Divide the total cost of the jeans by two to get the cost of a single pair
    cost_per_pair = total_excl_coats_shoes / 2
    result = cost_per_pair
    return result

print(solution())