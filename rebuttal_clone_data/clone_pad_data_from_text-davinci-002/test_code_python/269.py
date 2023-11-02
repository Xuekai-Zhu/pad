def solution():
     """John earned $18 on Saturday but he only managed to earn half that amount on Sunday. He earned $20 the previous weekend. How much more money does he need to earn to give him the $60 he needs to buy a new pogo stick?"""
     money_earned = [18, 9, 20]
     money_needed = 60
     total_money_earned = sum(money_earned)
     money_needed = money_needed - total_money_earned
     result = money_needed
     return result

print(solution())