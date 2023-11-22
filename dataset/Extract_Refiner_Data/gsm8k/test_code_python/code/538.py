def solution():
    
    # Define the prices of each fruit
    APPLE_PRICE = 1.5
    ORANGE_PRICE = 0.8
    PEACH_PRICE = 0.75

    # Define the quantities purchased
    num_apples = 3
    num_oranges = 5
    num_peaches = 6

    # Calculate the total cost of the fruit
    total_cost = (apple_PRICE * num_apples) + (orange_PRICE * num_oranges) + (peach_PRICE * num_peaches)

    # Calculate the change received
    change = 20 - total_cost

    # Display the change received
    result = change
    return result

print(solution())