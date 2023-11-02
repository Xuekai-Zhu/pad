def solution():
     opening_weekend = 120000000
     total_run = opening_weekend * 3.5
     percent_kept = 60
     company_revenue = total_run * (percent_kept / 100)
     production_cost = 60000000
     profit = company_revenue - production_cost
     result = profit
     return result

print(solution())