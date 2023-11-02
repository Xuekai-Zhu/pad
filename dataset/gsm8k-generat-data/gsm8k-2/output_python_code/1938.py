def solution():
    """Half of Jerome's money was $43. He gave $8 to Meg and thrice as much to Bianca. How much does Jerome have left?"""
    half_money = 43
    total_money = 2 * half_money
    meg_money = 8
    bianca_money = 3 * meg_money
    money_left = total_money - meg_money - bianca_money
    result = money_left
    return result

print(solution())