def solution():
    # Calculate the speed increase from supercharging the car
    supercharge_speed = 150 * 0.3  # 30% increase from supercharging the car

    # Calculate the new speed after supercharging
    new_speed = 150 + supercharge_speed

    # Calculate the speed increase from cutting weight
    weight_reduction_speed = new_speed * 0.15  # 15% increase from cutting weight

    # Calculate the final speed after cutting weight
    final_speed = new_speed + weight_reduction_speed + 10  # 10 mph increase from cutting weight

    result = final_speed
    return result

print(solution())