def solution():
    
    steady_flow_rate = 2/10 
    first_hour = steady_flow_rate * 60 
    double_flow_rate = 4/10 
    second_hour = double_flow_rate * 60 
    total_water = first_hour + second_hour 
    half_water = total_water / 2 
    result = half_water
    return result

print(solution())