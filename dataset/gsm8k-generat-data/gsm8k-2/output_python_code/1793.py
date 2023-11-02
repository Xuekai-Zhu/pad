def solution():
    """Joshua and Justin shared $40. Joshua’s share was thrice as much as Justin’s. How much is Joshua's share?"""
    total_money = 40
    ratio = 3
    joshua_share = (total_money / (ratio + 1)) * ratio
    result = joshua_share
    return result

print(solution())