def solution():
    # Define the cost of a small puzzle as x
    x = 0

    # Calculate the cost of a large puzzle
    large_puzzle_cost = 15

    # Solve for x using the information that a small puzzle and a large puzzle together cost $23
    x = (23 - large_puzzle_cost) / 2

    # Calculate the cost of 3 small puzzles
    small_puzzle_cost = 3 * x

    # Calculate the total cost of 1 large and 3 small puzzles
    total_cost = large_puzzle_cost + small_puzzle_cost
    result = total_cost
    return result

print(solution())