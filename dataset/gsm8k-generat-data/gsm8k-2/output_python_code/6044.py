def solution():
    """Billy has $25 less than twice the money Sam has. If Sam has $75, how much money do they have together?"""
    sam_money = 75
    billy_money = 2 * sam_money - 25
    total_money = sam_money + billy_money
    result = total_money
    return result

print(solution())