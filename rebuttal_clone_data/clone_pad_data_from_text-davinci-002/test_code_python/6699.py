def solution():
     number_of_rose_bushes = 20
     cost_of_rose_bush = 150
     cost_of_soil = 5
     cubic_feet_of_soil = 100
     hours_worked = 5
     days_worked = 4
     hourly_rate = 30
     total_cost_of_rose_bushes = number_of_rose_bushes * cost_of_rose_bush
     total_cost_of_soil = cubic_feet_of_soil * cost_of_soil
     total_cost_of_labor = hours_worked * days_worked * hourly_rate
     total_cost = total_cost_of_rose_bushes + total_cost_of_soil + total_cost_of_labor
     
     result = total_cost
     
     return result

print(solution())