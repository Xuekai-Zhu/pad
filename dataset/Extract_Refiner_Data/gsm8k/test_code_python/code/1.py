def solution():
    
    # Define the cost of one glass and the cost of every second glass
    GLASS_PRICE = 5
    SECOND_GLASS_PRICE = GLASS_PRICE * 0.6

    # Define the number of glasses Kylar wants to buy
    NUM_GLASSES = 16

    # Calculate the total cost of the glasses
    total_cost = NUM_GLASSES * GLASS_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())