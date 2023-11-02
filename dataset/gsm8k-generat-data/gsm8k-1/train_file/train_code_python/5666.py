def solution():
    """Leonard and his brother Michael bought presents for their father. Leonard bought a wallet at $50 and two pairs of sneakers at $100 each pair, while Michael bought a backpack at $100 and two pairs of jeans at $50 each pair. How much did they spend in all?"""
    leonard_spent = 50 + 2 * 100
    michael_spent = 100 + 2 * 50
    total_spent = leonard_spent + michael_spent
    result = total_spent
    return result

print(solution())