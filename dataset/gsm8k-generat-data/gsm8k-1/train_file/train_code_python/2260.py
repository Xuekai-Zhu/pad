def solution():
    """Greg and Katie went to Mrs. Scarlet's gold store to have their gold chests opened. They realized Greg had four times less gold than Katie when Mrs. Scarlet opened the chests. If the total amount of gold is 100, how much gold does Greg have?"""
    total_gold = 100
    ratio = 1 / 4
    katie_gold = (total_gold / 5) * 4
    greg_gold = total_gold - katie_gold
    result = greg_gold
    return result

print(solution())