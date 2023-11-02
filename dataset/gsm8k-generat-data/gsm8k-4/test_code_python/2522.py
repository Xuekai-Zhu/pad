def solution():
    """A large puzzle costs $15. A small puzzle and a large puzzle together cost $23. How much would you pay for 1 large and 3 small puzzles?"""
    # Define the price of a large puzzle and the total cost of a small and large puzzle
    large_puzzle_price = 15
    small_and_large_puzzle_price = 23

    # Calculate the price of a small puzzle
    small_puzzle_price = small_and_large_puzzle_price - large_puzzle_price

    # Calculate the total price of 1 large and 3 small puzzles
    total_price = (1 * large_puzzle_price) + (3 * small_puzzle_price)

    # return the result
    result = total_price
    return result

print(solution())