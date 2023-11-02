def solution():
    """Tammy has 10 orange trees from which she can pick 12 oranges each day. Tammy sells 6-packs of oranges for $2. How much money will Tammy have earned after 3 weeks if she sells all her oranges?"""
    trees = 10
    oranges_per_day = 12
    days_per_week = 7
    weeks = 3
    total_oranges = trees * oranges_per_day * days_per_week * weeks
    packs_of_oranges = total_oranges // 6
    price_per_pack = 2
    total_earnings = packs_of_oranges * price_per_pack
    result = total_earnings
    return result

print(solution())