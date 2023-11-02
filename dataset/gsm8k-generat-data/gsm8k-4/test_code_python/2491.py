def solution():
    """A candy store sold 20 pounds of fudge for $2.50/pound, 5 dozen chocolate truffles for $1.50 each and 3 dozen chocolate-covered pretzels at $2.00 each. How much money did the candy store make?"""
    # Define the sales and prices of each item
    fudge_sales = 20 * 2.5
    truffle_sales = 5 * 1.5 * 12
    pretzel_sales = 3 * 2 * 12

    # Calculate the total sales
    total_sales = fudge_sales + truffle_sales + pretzel_sales

    # Return the total sales
    result = total_sales
    return result

print(solution())