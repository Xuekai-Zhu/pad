def solution():
    original_speed = 150  # James' car's original speed is 150 mph

    # Supercharging the car increases the speed by 30%
    supercharged_speed = original_speed * 1.3  

    # Cutting the weight of the car increases the speed by 10 mph, which is a 15% increase from the supercharged speed
    final_speed = supercharged_speed * 1.15 + 10  

    result = final_speed
    return result

print(solution())