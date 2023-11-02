def solution():
    
    base_fine = 50
    speed_limit = 30
    mark_speed = 75
    over_speed = mark_speed - speed_limit
    fine = base_fine + (2 * over_speed)
    fine *= 2
    court_costs = 300
    lawyer_fee = 80 * 3
    total_cost = fine + court_costs + lawyer_fee
    result = total_cost
    return result

print(solution())