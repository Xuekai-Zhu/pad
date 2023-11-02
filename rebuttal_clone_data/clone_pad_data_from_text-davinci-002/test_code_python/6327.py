def solution():
     salary_increase = 480 * (10 / 100)
     travel_increase = 480 * (20 / 100)
     employees_without_increase = 480 - (salary_increase + travel_increase)
     result = employees_without_increase
     return result

print(solution())