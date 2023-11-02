def solution():
     pills_per_day = 2
     days_in_month = 30
     cost_per_pill = 1.5
     percent_coverage = 40
     total_cost = pills_per_day * days_in_month * cost_per_pill
     insurance_coverage = total_cost * (percent_coverage / 100)
     out_of_pocket_cost = total_cost - insurance_coverage
     result = out_of_pocket_cost
     return result

print(solution())