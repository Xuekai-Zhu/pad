def solution():
    # Find the price of a small puzzle
    small_puzzle = 23 - 15  # cost of small and large puzzle together minus cost of large puzzle
    # Find the total cost of 1 large and 3 small puzzles
    total_cost = 15*1 + small_puzzle*3
    result = total_cost
    return result

print(solution())