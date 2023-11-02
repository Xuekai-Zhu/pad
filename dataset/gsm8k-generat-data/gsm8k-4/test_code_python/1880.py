def solution():
    """Milo can roll downhill on his skateboard at twice the speed that he can run. And Milo's best friend, Cory, can drive his wheelchair at twice the speed that Milo can roll downhill on his skateboard. If Cory always drives his wheelchair at 12 miles per hour, how many miles can Milo run in two hours?"""
    # Define Milo's running speed
    running_speed = None

    # Define Milo's rolling downhill speed
    rolling_speed = running_speed * 2

    # Define Cory's driving speed
    driving_speed = rolling_speed * 2

    # Set Cory's driving speed to 12 miles per hour
    driving_speed = 12

    # Calculate the distance Milo runs in two hours
    running_distance = running_speed * 2

    # Return the result
    result = running_distance
    return result

print(solution())