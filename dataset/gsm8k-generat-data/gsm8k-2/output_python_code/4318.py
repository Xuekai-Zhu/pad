def solution():
    """Tammy has 10 orange trees from which she can pick 12 oranges each day. Tammy sells 6-packs of oranges for $2. How much money will Tammy have earned after 3 weeks if she sells all her oranges?"""
    trees = 10
    oranges_per_day = 12
    oranges_per_week = trees * oranges_per_day * 7
    oranges_per_pack = 6
    packs_per_week = oranges_per_week // oranges_per_pack
    price_per_pack = 2
    total_earnings = packs_per_week * price_per_pack * 3
    result = total_earnings
    return result

print(solution())