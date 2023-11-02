def solution():
    """Jackson has 5 times more money than Williams. Together, they have $150. How much money, in dollars, does Jackson have?"""
    total_money = 150
    ratio = 6  # 5x more money means Jackson has 6 times the money as Williams
    jackson_money = total_money / ratio * 5
    result = jackson_money
    return result

print(solution())