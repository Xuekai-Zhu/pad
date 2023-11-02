def solution():
     mowing_rate = 4
     weeding_rate = 8
     hours_mowing = 25
     hours_weeding = 3
     money_made_mowing = mowing_rate * hours_mowing
     money_made_weeding = weeding_rate * hours_weeding
     total_money_made = money_made_mowing + money_made_weeding
     result = total_money_made
     return result

print(solution())