def solution():
     goal = 1000
     money_earned = 300 + 40
     houses_visited = 4
     average_earning = 10
     money_left = goal - money_earned
     houses_needed = money_left / average_earning
     result = houses_needed

     return result

print(solution())