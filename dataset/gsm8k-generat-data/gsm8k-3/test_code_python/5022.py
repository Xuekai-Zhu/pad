def solution():
    """Georgie is a varsity player on a football team. He can run 40 yards within 5 seconds. If he can improve his speed by forty percent, how many yards will he be able to run within 10 seconds?"""
    # Define the original distance and time
    original_distance = 40
    original_time = 5

    # Define the improvement percentage
    improvement_percent = 40

    # Convert percentage to decimal
    improvement_decimal = improvement_percent / 100

    # Calculate the new speed and time
    new_speed = original_distance / original_time * (1 + improvement_decimal)
    new_time = 10

    # Calculate the new distance
    new_distance = new_speed * new_time

    # Display the new distance
    result = new_distance
    return result

print(solution())