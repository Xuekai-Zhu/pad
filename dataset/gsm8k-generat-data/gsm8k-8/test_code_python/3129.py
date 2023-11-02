def solution():
    # Calculate the cost of the rose bushes
    rose_bush_cost = 6 * 75
    rose_bush_cost_for_friend = 2 * 75
    rose_bush_cost_for_self = rose_bush_cost - rose_bush_cost_for_friend

    # Calculate the cost of the tiger tooth aloes
    aloe_cost = 2 * 100

    # Calculate the total cost of the plants for himself
    total_cost = rose_bush_cost_for_self + aloe_cost
    result = total_cost
    return result

print(solution())