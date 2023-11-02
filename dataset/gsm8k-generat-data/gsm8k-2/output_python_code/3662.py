def solution():
    """If Beth had $35 more, she would have $105. If Jan had $10 less, he would have the same money as Beth has. How much money do Beth and Jan have altogether?"""
    beth_money = 105 - 35
    jan_money = beth_money - 10
    total_money = beth_money + jan_money
    result = total_money
    return result

print(solution())