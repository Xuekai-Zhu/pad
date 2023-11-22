def solution():
    
    # Define the distance between the dragon and the distance of the gemstone
    GEMON_DISTANCE = 1000

    # Define the distance between the gold javelin and the distance of the gemstone when Polly held the gemstone
    GEMON_GOLD_DISTANCE = 400

    # Calculate the distance between the gold javelin and the distance of the gemstone when Polly held the gemstone
    GEMON_GOLD_DISTANCE = GEMON_DISTANCE * 3

    # Calculate the distance outside of the reach of the dragon's flames
    outside_distance = GEMON_DISTANCE - GEMON_GOLD_DISTANCE

    # Display the distance outside of the reach of the dragon's flames
    result = outside_distance
    return result

print(solution())