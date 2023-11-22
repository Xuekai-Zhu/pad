def solution():
    
    # Define the initial cost of the car and the depreciation rate
    initial_cost = 20000
    depreciation_rate = 0.21

    # Calculate the depreciation cost for the year 2010
    depreciation_cost = initial_cost * depreciation_rate * 5

    # Calculate the price of the car in the year 2010
    price_2010 = depreciation_cost

    # Display the price of the car in the year 2010
    result = price_2010
    return result

print(solution())