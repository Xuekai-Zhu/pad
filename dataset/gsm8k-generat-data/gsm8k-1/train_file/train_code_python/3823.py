def solution():
    """Maria gave a third of her money to her friend Isha, half of what she gave to Florence. If Florence received three times as much money as Maria's cousin Rene, and Rene received $300, how much money did Maria give her three friends?"""
    rene_money = 300
    florence_money = 3 * rene_money
    isha_money = florence_money / 2
    total_money_given = isha_money + florence_money + rene_money
    result = total_money_given
    return result

print(solution())