def solution():
    """Keaton has a farm of oranges and apples. He can harvest his oranges every 2 months and can sell the harvest for $50. He can harvest his apples every 3 months and can sell this harvest for $30. How much money can Keaton earn every year?"""
    oranges_per_year = 6 # 12 / 2
    apples_per_year = 4 # 12 / 3
    orange_income = oranges_per_year * 50
    apple_income = apples_per_year * 30
    total_income = orange_income + apple_income
    result = total_income
    return result

print(solution())