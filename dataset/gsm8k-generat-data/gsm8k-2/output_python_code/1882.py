def solution():
    """Jim spends 8 hours scuba diving. In that time he finds a treasure chest with 100 gold coins in it. He also finds 2 smaller bags that have half as much gold each. How much gold does he find per hour?"""
    total_time = 8
    total_gold = 100 + 2 * (0.5 * 100)
    gold_per_hour = total_gold / total_time
    result = gold_per_hour
    return result

print(solution())