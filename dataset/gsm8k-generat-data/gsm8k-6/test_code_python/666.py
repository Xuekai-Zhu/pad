def solution():
    # Find the amount of money Jackson and Williams have
    total_money = 150
    # Let x be the amount of money Williams has
    x = total_money / 6  # 1 part out of 6 parts belongs to Williams
    # Jackson has 5 times more money than Williams, so he has 5x
    jackson_money = 5 * x
    result = jackson_money
    return result

print(solution())