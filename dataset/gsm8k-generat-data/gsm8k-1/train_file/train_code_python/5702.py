def solution():
    """Frank is making hamburgers and he wants to sell them to make $50. Frank is selling each hamburger for $5 and 2 people purchased 4 and another 2 customers purchased 2 hamburgers. How many more hamburgers does Frank need to sell to make $50?"""
    hamburgers_sold = (2 * 4) + (2 * 2)
    total_money = hamburgers_sold * 5
    additional_sales_needed = (50 - total_money) / 5
    result = additional_sales_needed
    return result

print(solution())