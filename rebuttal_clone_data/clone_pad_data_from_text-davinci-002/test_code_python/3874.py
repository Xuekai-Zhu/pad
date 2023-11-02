def solution():
     cakes_per_day = 4
     days_per_week = 5
     weeks = 4
     price_per_cake = 8
     total_cakes = cakes_per_day * days_per_week * weeks
     total_sales = total_cakes * price_per_cake
     result = total_sales
     return result

print(solution())