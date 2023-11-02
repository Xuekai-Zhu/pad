def solution():
    """Bridge and Sarah have $3 between them. If Bridget has 50 cents more than Sarah, how many cents does Sarah have?"""
    total_money = 300  # convert dollars to cents
    bridget_money = (total_money + 50) / 2
    sarah_money = total_money - bridget_money
    result = sarah_money
    return result

print(solution())