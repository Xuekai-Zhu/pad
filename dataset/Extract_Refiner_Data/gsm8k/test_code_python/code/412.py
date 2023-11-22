def solution():
    
    # Define the number of camels and dromedaries
    camels = 180 // 2
    dromedaries = 304 // 1

    # Calculate the number of dromedaries
    dromedaries = dromedaries - camels

    # Display the number of dromedaries
    result = dromedaries
    return result

print(solution())