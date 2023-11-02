def solution():
    """Kenneth has $50 to go to the store. Kenneth bought 2 baguettes and 2 bottles of water. Each baguette cost $2 and each bottle of water cost $1. How much money does Kenneth have left?"""
    total_spent = (2*2) + (2*1)
    remaining_money = 50 - total_spent
    result = remaining_money
    return result

print(solution())