def solution():
    original_speed = 150
    supercharge_increase = 0.3
    weight_reduction_increase = 0.1
    weight_reduction_percentage = 0.15
    
    # Calculate the speed increase from supercharging
    supercharge_speed_increase = original_speed * supercharge_increase

    # Calculate the new speed after supercharging
    supercharged_speed = original_speed + supercharge_speed_increase

    # Calculate the weight reduction
    weight_reduction = supercharged_speed * weight_reduction_percentage

    # Calculate the speed increase from weight reduction
    weight_reduction_speed_increase = supercharged_speed * weight_reduction_increase

    # Calculate the new speed after weight reduction
    new_speed = supercharged_speed - weight_reduction + weight_reduction_speed_increase
    result = new_speed
    return result

print(solution())