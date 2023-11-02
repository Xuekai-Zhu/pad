def solution():
    """If Beth had $35 more, she would have $105. If Jan had $10 less, he would have the same money as Beth has. How much money do Beth and Jan have altogether?"""
    beth_current_money = 105 - 35
    jan_current_money = beth_current_money + 10
    total_money = beth_current_money + jan_current_money
    result = total_money
    return result

print(solution())