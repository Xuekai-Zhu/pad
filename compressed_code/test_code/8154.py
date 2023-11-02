def solution():
    
    total_burgers = 30
    double_burgers = total_burgers // 2
    single_burgers = total_burgers - double_burgers
    burgers_on_grill = 5
    time_per_burger = 8 
    total_time = ((double_burgers * 2) + single_burgers) * time_per_burger / burgers_on_grill
    result = total_time
    return result

print(solution())