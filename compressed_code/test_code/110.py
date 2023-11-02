def solution():
    
    lottery_win = 50
    tax = 0.2 * lottery_win
    processing_fee = 5
    take_home = lottery_win - tax - processing_fee
    result = take_home
    return result

print(solution())