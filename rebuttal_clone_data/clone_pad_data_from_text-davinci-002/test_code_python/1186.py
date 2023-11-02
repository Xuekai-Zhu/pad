def solution():
     permit_cost = 250
     contractor_cost = 150
     days_worked = 3
     hours_per_day = 5
     total_hours = days_worked * hours_per_day
     total_contractor_cost = total_hours * contractor_cost
     inspector_cost = total_contractor_cost * 0.8
     total_cost = permit_cost + total_contractor_cost + inspector_cost
     result = total_cost
     return result

print(solution())