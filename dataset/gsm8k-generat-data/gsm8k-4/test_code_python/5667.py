def solution():
    """Leonard and his brother Michael bought presents for their father. Leonard bought a wallet at $50 and two pairs of sneakers at $100 each pair, while Michael bought a backpack at $100 and two pairs of jeans at $50 each pair. How much did they spend in all?"""
    # Calculate Leonard's total spending
    leonard_spending = 50 + (2 * 100)

    # Calculate Michael's total spending
    michael_spending = 100 + (2 * 50)

    # Calculate the total spending of both brothers
    total_spending = leonard_spending + michael_spending

    result = total_spending
    return result

print(solution())