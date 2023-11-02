def solution():
     pool_cleaning_cost = 150
     pool_cleaning_tip = 15
     pool_cleaning_total = pool_cleaning_cost + pool_cleaning_tip
     pool_chemical_cost = 200
     pool_cleaning_frequency = 2
     total_monthly_cost = (pool_cleaning_total * pool_cleaning_frequency) + pool_chemical_cost
     result = total_monthly_cost
     return result

print(solution())