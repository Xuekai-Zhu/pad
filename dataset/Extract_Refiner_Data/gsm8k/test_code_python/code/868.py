def solution():
    
    # Define the cost of each type of bottle
    SODA_PRICE = 21
    WATER_PRICE = 8

    # Define the number of bottles of each type of bottle David wants to buy
    soda_bottles = 3
    water_bottles = 2

    # Calculate the total cost of the soda
    soda_cost = soda_bottles * SODA_PRICE

    # Calculate the total cost of the water
    water_cost = water_bottles * WATER_PRICE

    # Calculate the total cost of the purchase
    total_cost = soda_cost + water_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())