def solution():
     entrance_fee = 5
     monthly_visits = 1
     months_per_year = 12
     years = 3
     total_cost = (entrance_fee * monthly_visits * months_per_year * years) + ((7 - 5) * (4 * years))
     result = total_cost
     return result

print(solution())