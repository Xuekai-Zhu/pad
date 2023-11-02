def solution():
     pills_per_day = 2
     days_per_month = 30
     months_per_year = 6
     doctor_visit_cost = 400
     pill_cost = 5
     insurance_coverage = 0.8
     
     total_pills = pills_per_day * days_per_month * months_per_year
     total_pill_cost = total_pills * pill_cost
     total_insurance_coverage = total_pill_cost * insurance_coverage
     total_cost = total_insurance_coverage + doctor_visit_cost
     
     result = total_cost
     return result

print(solution())