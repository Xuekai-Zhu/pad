def solution():
     lion_cost = 10
     lion_earnings = 200
     lion_profit = lion_earnings / 2
     star_cost = 25
     star_earnings = lion_profit + (star_cost - lion_cost)
     result = star_earnings
     return result

print(solution())