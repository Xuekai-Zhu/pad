def solution():
    """James and Ali together own $250. If you know that James owns $40 more than Ali, then calculate the amount owned by James."""
    total_ownership = 250
    diff = 40
    james_share = (total_ownership + diff) / 2
    result = james_share
    return result

print(solution())