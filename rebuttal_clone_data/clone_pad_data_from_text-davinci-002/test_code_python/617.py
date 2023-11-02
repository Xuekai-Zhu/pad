def solution():
     base_fine = 50
     over_limit_fee = 2
     over_limit_speed = 45
     fines_doubled = True
     court_costs = 300
     lawyer_costs = 80
     lawyer_hours = 3
     
     over_limit_fine = over_limit_fee * over_limit_speed
     if fines_doubled:
         over_limit_fine = over_limit_fine * 2
     total_fine = base_fine + over_limit_fine + court_costs + (lawyer_costs * lawyer_hours)
     result = total_fine
     
     return result

print(solution())