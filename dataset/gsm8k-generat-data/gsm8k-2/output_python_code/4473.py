def solution():
    """Alison has half as much money as Brittany. Brittany has 4 times as much money as Brooke. Brooke has twice as much money as Kent. If Kent has $1,000, how much money does Alison have?"""
    kent_money = 1000
    brooke_money = 2 * kent_money
    brittany_money = 4 * brooke_money
    alison_money = brittany_money / 2
    result = alison_money
    return result

print(solution())