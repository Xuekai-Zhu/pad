def solution():
    """Keaton has a farm of oranges and apples. He can harvest his oranges every 2 months and can sell the harvest for $50. He can harvest his apples every 3 months and can sell this harvest for $30. How much money can Keaton earn every year?"""
    oranges_per_year = 6
    apple_per_year = 4
    orange_profit = 50
    apple_profit = 30
    total_profit = oranges_per_year * orange_profit + apple_per_year * apple_profit
    result = total_profit
    return result

print(solution())