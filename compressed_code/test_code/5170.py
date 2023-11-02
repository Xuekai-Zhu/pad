def solution():
    
    
    inches_before_cut = 9
    inches_after_cut = 6
    inches_cut_per_cycle = inches_before_cut - inches_after_cut
    cycles_per_year = 12 / (inches_cut_per_cycle / 1.5)

    
    haircut_cost = 45
    tip_percent = 0.2
    tip_amount = haircut_cost * tip_percent
    total_cost_per_haircut = haircut_cost + tip_amount

    
    total_cost = total_cost_per_haircut * cycles_per_year
    result = total_cost
    return result

print(solution())