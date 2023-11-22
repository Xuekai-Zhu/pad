def solution():
    
    # Define the weight of each chocolate bar and candied apple
    CHOCOLATE_BAR_WEIGHT = 40
    CANDY_APPLE_WEIGHT = CHOCOLATE_BAR_WEIGHT / 2

    # Calculate the total weight of the chocolate bars and candied apples
    total_weight = (25 * CHOCOLATE_BAR_WEIGHT) + (80 * CANDY_APPLE_WEIGHT)

    # Display the total weight
    result = total_weight
    return result

print(solution())