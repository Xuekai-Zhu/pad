def solution():
    """Saheed made four times as much money as Kayla. Kayla made $30 less than Vika. Vika made $84. How many dollars did Saheed make?"""
    vika_money = 84
    kayla_money = vika_money - 30
    saheed_money = 4 * kayla_money
    result = saheed_money
    return result

print(solution())