def solution():
    
    admission_price = 12
    tour_price = 6
    group_1_size = 10
    group_2_size = 5
    group_1_cost = admission_price * group_1_size + tour_price * group_1_size
    group_2_cost = admission_price * group_2_size
    total_earnings = group_1_cost + group_2_cost
    result = total_earnings
    return result

print(solution())