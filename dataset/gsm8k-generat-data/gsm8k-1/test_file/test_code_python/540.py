def solution():
    """Jeff and Brad are trying to divide 100 dollars between them. Jeff gets 4 times as much as Brad. How much does Jeff get in dollars?"""
    total_money = 100
    ratio = 4
    brad_share = total_money / (1 + ratio)
    jeff_share = brad_share * ratio
    result = jeff_share
    return result

print(solution())