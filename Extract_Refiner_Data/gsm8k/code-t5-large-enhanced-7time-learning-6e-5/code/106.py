def solution():
    
    # Calculate the number of roll-ups that Beatrice ate
    beatrice_rollups = 2 * 24

    # Calculate the number of roll-ups that Marcell ate
    marcell_rollups = 3 * 14

    # Calculate the total number of roll-ups they ate
    total_rollups = beatrice_rollups + marcell_rollups

    # Calculate the average number of roll-ups they ate
    average_rollups = total_rollups / 2

    # Display the average number of roll-ups they ate
    result = average_rollups
    return result

print(solution())