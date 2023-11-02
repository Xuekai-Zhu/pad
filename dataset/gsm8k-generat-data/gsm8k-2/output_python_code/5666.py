def solution():
    """Leonard and his brother Michael bought presents for their father. Leonard bought a wallet at $50 and two pairs of sneakers at $100 each pair, while Michael bought a backpack at $100 and two pairs of jeans at $50 each pair. How much did they spend in all?"""
    leonard_total = 50 + 2*100
    michael_total = 100 + 2*50
    total_spent = leonard_total + michael_total
    result = total_spent
    return result

print(solution())