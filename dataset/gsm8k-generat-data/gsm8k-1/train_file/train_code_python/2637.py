def solution():
    """Bridge and Sarah have $3 between them. If Bridget has 50 cents more than Sarah, how many cents does Sarah have?"""
    total_money = 300  # $3 in cents
    # let x be the amount of money Sarah has in cents
    # then Bridget has x + 50 cents
    money_sum = x + (x + 50)
    if money_sum == total_money:
        sarah_money = x
        result = sarah_money
    else:
        result = "No solution"
    return result

print(solution())