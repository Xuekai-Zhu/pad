def solution():
    """Tom has a quarter as much money as Nataly. Nataly has three times as much money as Raquel. How much money do Tom, Raquel, and Nataly have combined if Raquel has $40?"""
    raquel_money = 40
    nataly_money = raquel_money * 3
    tom_money = nataly_money / 4
    total_money = raquel_money + nataly_money + tom_money
    result = total_money
    return result

print(solution())