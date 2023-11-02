def solution():
    """Alexander Bought 22 more joggers than Tyson. Christopher bought twenty times as many joggers as Tyson. If Christopher bought 80 joggers, how many more joggers does Christopher buy than Alexander?"""
    # Let x be the number of joggers Tyson bought
    # Then Alexander bought x + 22 joggers
    # And Christopher bought 20x joggers
    # We know that Christopher bought 80 joggers, so:
    # 20x = 80
    # x = 4
    # Therefore:
    # Tyson bought 4 joggers
    # Alexander bought 26 joggers
    # Christopher bought 80 joggers
    # Christopher bought 80 - 26 = 54 more joggers than Alexander
    result = 54
    return result

print(solution())