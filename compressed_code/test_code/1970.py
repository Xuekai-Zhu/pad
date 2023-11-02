def solution():
    
    large_puzzle_cost = 15
    small_puzzle_cost = 23 - large_puzzle_cost
    total_cost = 1 * large_puzzle_cost + 3 * small_puzzle_cost
    result = total_cost
    return result

print(solution())