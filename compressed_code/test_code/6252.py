def solution():
    
    base_fine = 50
    speed_over_limit = 75 - 30
    fine_per_mph_over = 2
    increased_fine = base_fine + (speed_over_limit * fine_per_mph_over)
    fine_in_school_zone = increased_fine * 2
    court_costs = 300
    lawyer_fee_per_hour = 80
    total_lawyer_fee = lawyer_fee_per_hour * 3
    total_cost = fine_in_school_zone + court_costs + total_lawyer_fee
    result = total_cost
    return result

print(solution())