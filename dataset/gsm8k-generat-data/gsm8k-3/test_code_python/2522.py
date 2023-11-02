def solution():
    """A large puzzle costs $15. A small puzzle and a large puzzle together cost $23. How much would you pay for 1 large and 3 small puzzles?"""
    # Define the cost of a large puzzle and the cost of a small puzzle
    LARGE_PUZZLE_COST = 15
    SMALL_PUZZLE_COST = (23 - LARGE_PUZZLE_COST) / 2

    # Calculate the cost of 1 large and 3 small puzzles
    total_cost = 1 * LARGE_PUZZLE_COST + 3 * SMALL_PUZZLE_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())