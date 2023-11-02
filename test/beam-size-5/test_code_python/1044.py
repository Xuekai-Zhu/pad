def solution():
    
    # Define the initial cost of the car and the depreciation rate
    initial_cost = 20000
    depreciation_rate = 0.21

    # Calculate the price of the car after the depreciation rate
    price_after_depreciation = initial_cost * depreciation_rate

    # Calculate the price of the car in the year 2010
    price_in_year_2010 = price_after_depreciation * 365

    # Display the price of the car in the year 2010
    result = price_in_year_2010
    return result

print(solution())