def solution():
    # Define original speed
    original_speed = 150

    # Calculate speed increase after supercharging
    supercharge_increase = original_speed * 0.3

    # Calculate new speed after supercharging
    supercharged_speed = original_speed + supercharge_increase

    # Calculate weight reduction increase
    weight_reduction_increase = 10

    # Calculate new speed after weight reduction
    weight_reduced_speed = supercharged_speed + weight_reduction_increase

    result = weight_reduced_speed
    return result

print(solution())