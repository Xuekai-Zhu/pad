def solution():
    """Carly is making burgers for a neighborhood BBQ. Each burger needs to be cooked for 4 minutes on each side. Carly can fit 5 burgers on the grill at once. If half her 30 guests want 2 burgers and the other half each want 1, how long will it take Carly to cook all the burgers?"""
    total_burgers = 30
    double_burgers = total_burgers // 2
    single_burgers = total_burgers - double_burgers
    burgers_on_grill = 5
    time_per_burger = 8 # 4 minutes per side = 8 minutes total
    total_time = ((double_burgers * 2) + single_burgers) * time_per_burger / burgers_on_grill
    result = total_time
    return result

print(solution())