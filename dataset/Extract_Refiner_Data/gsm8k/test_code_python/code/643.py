def solution():
    
    # Define the speeds of digging through soil and clay
    SOIL_SPEED = 4
    CLAY_SPEED = SOIL_SPEED / 2

    # Define the amount of soil and clay to dig
    soil_amount = 24
    clay_amount = 8

    # Calculate the total time to dig the well
    total_time = (soil_amount / SOIL_SPEED) + (clay_amount / CLAY_SPEED)

    # Display the total time
    result = total_time
    return result

print(solution())