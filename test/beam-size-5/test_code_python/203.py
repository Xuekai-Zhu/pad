def solution():
    
    # Define the weight of each chocolate bar
    CHOCOLATE_BAR_WEIGHT = 40

    # Define the weight of each candied apple
    APPLE_WEIGHT = CHOCOLATE_BAR_WEIGHT * 2

    # Define the number of chocolate bars and candied apples
    num_chocolate_bars = 25
    num_apples = 80

    # Calculate the total weight of the chocolate bars
    chocolate_bar_weight = num_chocolate_bars * CHOCOLATE_BAR_WEIGHT

    # Calculate the total weight of the candied apples
    candied_apple_weight = num_apples * APPLE_WEIGHT

    # Calculate the total weight of the candy in grams
    total_weight = chocolate_bar_weight + candied_apple_weight

    # Display the total weight in grams
    result = total_weight
    return result

print(solution())