def solution():
    """Milo can roll downhill on his skateboard at twice the speed that he can run.  And Milo's best friend, Cory, can drive his wheelchair at twice the speed that Milo can roll downhill on his skateboard.  If Cory always drives his wheelchair at 12 miles per hour, how many miles can Milo run in two hours?"""
    # Define Milo's speeds relative to his running speed
    SKATEBOARD_SPEED = 2
    WHEELCHAIR_SPEED = 4

    # Define Cory's driving speed
    CORY_SPEED = 12

    # Calculate Milo's running speed
    running_speed = CORY_SPEED / WHEELCHAIR_SPEED / SKATEBOARD_SPEED

    # Calculate Milo's distance traveled in two hours
    distance = running_speed * 2

    # Display the distance traveled
    result = distance
    return result

print(solution())