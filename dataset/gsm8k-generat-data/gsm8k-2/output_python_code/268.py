def solution():
    """John earned $18 on Saturday but he only managed to earn half that amount on Sunday. He earned $20 the previous weekend. How much more money does he need to earn to give him the $60 he needs to buy a new pogo stick?"""
    saturday_earnings = 18
    sunday_earnings = saturday_earnings / 2
    previous_weekend_earnings = 20
    total_earnings = saturday_earnings + sunday_earnings + previous_weekend_earnings
    money_needed = 60
    money_to_earn = money_needed - total_earnings
    result = money_to_earn
    return result

print(solution())