def solution():
    """Frank is making hamburgers and he wants to sell them to make $50. Frank is selling each hamburger for $5 and 2 people purchased 4 and another 2 customers purchased 2 hamburgers. How many more hamburgers does Frank need to sell to make $50?"""
    total_sales = 0
    for i in [4, 4, 2, 2]:
        total_sales += i*5

    hamburgers_needed = (50 - total_sales) / 5
    result = hamburgers_needed
    return result

print(solution())