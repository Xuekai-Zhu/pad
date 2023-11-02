def solution():
    """A supermarket has pints of strawberries on sale. They sold 54 pints and made $216, which was $108 less than they would have made selling the same number of pints without the sale. How many more dollars does a pint of strawberries cost when not on sale?"""
    # Let's assume that the price of a pint of strawberries on sale is x dollars
    # Then the total revenue from the sale of 54 pints is 54x dollars
    # We are told that they made $216, so we can write the equation:
    # 54x = 216

    # Solving for x, we get:
    x = 4

    # This means that a pint of strawberries on sale costs $4

    # We are also told that without the sale, they would have made $108 more
    # This means that they would have made $324 selling the same number of pints without the sale
    # Let's assume that the cost of a pint of strawberries without the sale is y dollars
    # Then the total revenue from the sale of 54 pints without the sale is 54y dollars
    # We are told that this is $108 more than what they made on the sale, so we can write the equation:
    # 54y = 324

    # Solving for y, we get:
    y = 6

    # This means that a pint of strawberries without the sale costs $6

    # Finally, we can answer the question:
    # How many more dollars does a pint of strawberries cost when not on sale?
    # The answer is the difference between the cost of a pint with the sale and without the sale:
    difference = y - x

    result = difference
    return result

print(solution())