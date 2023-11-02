def solution():
     revenue = 3000
     salary_ratio = 4
     stock_ratio = 11
     salary_amount = revenue * (salary_ratio / (salary_ratio + stock_ratio))
     result = salary_amount
     return result

print(solution())