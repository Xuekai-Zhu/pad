def solution():
    """John decides to stop delivering the newspapers he is supposed to deliver and instead steals them to recycle them for cash.
    The Monday-Saturday papers weigh 8 ounces each. The Sunday paper weighs twice as much. He is supposed to deliver 250 papers a day.
    He doesn't deliver them for 10 weeks. If one ton of paper recycles for $20, how much did he make?"""
    days_not_delivering = 10 * 7
    total_papers_not_delivered = days_not_delivering * 250
    total_weight_not_delivered = (total_papers_not_delivered * 8 / 16) + ((total_papers_not_delivered / 7) * 16)
    total_weight_tons = total_weight_not_delivered / 2000
    total_money = total_weight_tons * 20
    result = total_money
    return result

print(solution())