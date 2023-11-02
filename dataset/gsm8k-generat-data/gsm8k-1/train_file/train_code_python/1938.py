def solution():
    """Half of Jerome's money was $43. He gave $8 to Meg and thrice as much to Bianca. How much does Jerome have left?"""
    half_money = 43
    initial_money = half_money * 2
    money_left = initial_money - 8 - (3*8)
    result = money_left
    return result

print(solution())