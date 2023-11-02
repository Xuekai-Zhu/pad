def solution():
    large_puzzle_cost = 15  # A large puzzle costs $15
    small_puzzle_cost = (23 - large_puzzle_cost) / 2  # A small puzzle costs the difference between the total cost of two puzzles and the cost of a large puzzle, divided by 2

    # Calculate the cost of 1 large puzzle and 3 small puzzles
    total_cost = large_puzzle_cost * 1 + small_puzzle_cost * 3
    result = total_cost
    return result

print(solution())