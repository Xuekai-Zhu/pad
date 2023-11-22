def solution():
    
    # Define the cost of each item
    BREAD_COST = 3
    SANDWICH_COST = 7

    # Define the number of sandwiches per loaf
    SANDWICHES_PER_LOAF = 10

    # Define the number of cheeses sold
    NUM_CHEESES = 10

    # Calculate the total number of sandwiches sold
    total_sandwiches = SANDWICHES_PER_LOAF * NUM_CHEESES

    # Calculate the total cost of the cheeses
    cheeses_cost = total_sandwiches * SANDWICH_COST

    # Calculate the total revenue from selling the cheeses
    revenue = NUM_CHEESES * 7

    # Calculate the net profit
    net_profit = revenue - cheeses_cost - bread_cost

    # Display the net profit
    result = net_profit
    return result

print(solution())