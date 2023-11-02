def solution():
    kiddie_scoop = 3
    regular_scoop = 4
    double_scoop = 6
    number_of_kiddie_scoops = 2
    number_of_regular_scoops = 2
    number_of_double_scoops = 3
    cost_of_kiddie_scoops = number_of_kiddie_scoops * kiddie_scoop
    cost_of_regular_scoops = number_of_regular_scoops * regular_scoop
    cost_of_double_scoops = number_of_double_scoops * double_scoop
    total_cost = cost_of_kiddie_scoops + cost_of_regular_scoops + cost_of_double_scoops
    result = total_cost
    
    return result

print(solution())