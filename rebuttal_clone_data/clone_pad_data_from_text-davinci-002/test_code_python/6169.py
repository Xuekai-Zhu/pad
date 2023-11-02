def solution():
     marathon_distance = 26.3
     miles_run_first_month = 3
     total_months = math.log(marathon_distance/miles_run_first_month, 2)
     rounded_months = math.ceil(total_months)
     result = rounded_months
     return result

print(solution())