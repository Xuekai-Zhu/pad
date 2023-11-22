def solution():
    
    # Define the profit and the number of chickens
    PROFIT = 2000
    NUM_CHOCKENS = 300

    # Calculate the number of chickens Isaias plans to sell
    num_sold = NUM_CHOCKENS * (3/5)

    # Calculate the total cost of the chickens he plans to sell
    total_cost = num_sold * 50

    # Display the total cost
    result = total_cost
    return result

print(solution())