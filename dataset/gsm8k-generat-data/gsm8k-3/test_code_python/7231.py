def solution():
    """Tyler has $100. If he buys 8 scissors for $5 each and 10 erasers for $4 each, how much of his money remains?"""
    # Define the prices of the scissors and erasers
    SCISSOR_PRICE = 5
    ERASER_PRICE = 4

    # Define the number of scissors and erasers Tyler buys
    num_scissors = 8
    num_erasers = 10

    # Calculate the total cost of the scissors and erasers
    total_cost = (num_scissors * SCISSOR_PRICE) + (num_erasers * ERASER_PRICE)

    # Calculate how much money Tyler has remaining
    remaining_money = 100 - total_cost

    # Display the remaining money
    result = remaining_money
    return result

print(solution())