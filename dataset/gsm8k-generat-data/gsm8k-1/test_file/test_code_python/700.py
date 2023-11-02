def solution():
    """Gerald and Julia divided $100 in the ratio 3:2. If Gerald spent $10 on a book, how much money did he have left?"""
    total_money = 100
    gerald_share = 3
    julia_share = 2
    gerald_money = (gerald_share / (gerald_share + julia_share)) * total_money
    gerald_money -= 10 # Gerald spent $10 on a book
    result = gerald_money
    return result

print(solution())