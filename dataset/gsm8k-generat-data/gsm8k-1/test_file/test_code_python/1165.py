def solution():
    """Ronnie was given $5 while Rissa was given thrice as much. After each of them had given an equal amount of money to their little sister, Rissa is left with 4/5 of her money. How much is left in Ronnie's money?"""
    ronnie_money = 5
    rissa_money = ronnie_money * 3
    total_money_given = (ronnie_money + rissa_money) / 2
    rissa_money_left = rissa_money - total_money_given
    ronnie_money_left = ronnie_money - total_money_given
    result = ronnie_money_left
    return result

print(solution())