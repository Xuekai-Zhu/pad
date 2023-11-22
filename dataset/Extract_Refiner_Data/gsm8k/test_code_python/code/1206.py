def solution():
    
    # Define the number of packs filled up and the number of balloons per pack
    PACKS_FILLED = 10
    BALLOONS_PER_PACK = 30

    # Calculate the total number of balloons
    total_balloons = PACKS_FILLED * BALLOONS_PER_PACK

    # Subtract the number of balloons left after the afternoon
    balloons_left = total_balloons - 12

    # Display the number of balloons thrown
    result = balloons_left
    return result

print(solution())