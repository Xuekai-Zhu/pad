def solution():
     tv_cost = 1700
     hourly_wage = 10
     work_hours_per_week = 30
     hours_needed_to_work = tv_cost / hourly_wage
     additional_hours_needed = hours_needed_to_work - work_hours_per_week
     result = additional_hours_needed
     return result

print(solution())