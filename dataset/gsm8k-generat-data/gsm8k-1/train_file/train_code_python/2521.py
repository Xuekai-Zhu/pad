def solution():
    """A large puzzle costs $15. A small puzzle and a large puzzle together cost $23. How much would you pay for 1 large and 3 small puzzles?"""
    large_puzzle_cost = 15
    small_puzzle_cost = (23 - large_puzzle_cost) / 2
    total_cost = (1 * large_puzzle_cost) + (3 * small_puzzle_cost)
    result = total_cost
    return result

print(solution())