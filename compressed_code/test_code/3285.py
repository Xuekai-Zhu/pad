def solution():
    
    apple_cost = 2
    banana_cost = 1
    orange_cost = 3
    total_cost = (12 * apple_cost) + (4 * banana_cost) + (4 * orange_cost)
    total_pieces = 12 + 4 + 4
    average_cost = total_cost / total_pieces
    result = average_cost
    return result

print(solution())