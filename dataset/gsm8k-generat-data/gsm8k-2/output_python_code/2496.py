def solution():
    """Tim won a $100 raffle. He gave away 20% to his friend. How much did he keep?"""
    total_money = 100
    friend_share = 0.2 * total_money
    tim_kept = total_money - friend_share
    result = tim_kept
    return result

print(solution())