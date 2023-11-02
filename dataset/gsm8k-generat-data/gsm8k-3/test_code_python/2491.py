def solution():
    """A candy store sold 20 pounds of fudge for $2.50/pound, 5 dozen chocolate truffles for $1.50 each and 3 dozen chocolate-covered pretzels at $2.00 each.  How much money did the candy store make?"""
    # Calculate the revenue from the fudge
    fudge_revenue = 20 * 2.5

    # Calculate the revenue from the chocolate truffles
    truffle_revenue = 5 * 12 * 1.5

    # Calculate the revenue from the chocolate-covered pretzels
    pretzel_revenue = 3 * 12 * 2.0

    # Calculate the total revenue
    total_revenue = fudge_revenue + truffle_revenue + pretzel_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())