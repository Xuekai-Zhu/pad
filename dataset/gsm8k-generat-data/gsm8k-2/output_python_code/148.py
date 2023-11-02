def solution():
    """Winwin won $50 in a lottery. She paid 20% for the tax and she paid $5 for the processing fee. How much was she able to take home?"""
    lottery_win = 50
    tax = 0.2 * lottery_win
    processing_fee = 5
    take_home = lottery_win - tax - processing_fee
    result = take_home
    return result

print(solution())