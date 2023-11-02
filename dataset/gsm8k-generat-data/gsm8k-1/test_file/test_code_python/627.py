def solution():
    """In a jewelers store, the price of a gold Jewell is 4/5 times as much as the price of a diamond Jewell. The cost of a silver Jewell is $400 less than the price of gold. If a diamond Jewell is $2000, find the total price for all three jewels."""
    diamond_price = 2000
    gold_price = (4/5) * diamond_price
    silver_price = gold_price - 400
    total_price = diamond_price + gold_price + silver_price
    result = total_price
    return result

print(solution())