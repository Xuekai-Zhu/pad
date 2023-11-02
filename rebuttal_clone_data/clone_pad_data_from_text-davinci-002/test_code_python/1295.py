def solution():
     total_peaches = 15
     peaches_sold_friends = 10
     peaches_sold_relatives = 4
     peaches_left = total_peaches - peaches_sold_friends - peaches_sold_relatives
     money_earned_friends = peaches_sold_friends * 2
     money_earned_relatives = peaches_sold_relatives * 1.25
     total_money_earned = money_earned_friends + money_earned_relatives
     result = total_money_earned
     return result

print(solution())