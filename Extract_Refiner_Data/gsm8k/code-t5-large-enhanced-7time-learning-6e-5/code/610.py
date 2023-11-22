def solution():
    
    # Define the number of loads of laundry per week and the cost per gallon of water
    LOADS_PER_WEEK = 2
    GALLONS_PER_LOAD = 20
    COST_PER_GALLON = 0.15

    # Calculate the total number of loads of laundry in a year
    total_loads = LOADS_PER_WEEK * 52

    # Calculate the total number of gallons of water used in a year
    total_gallons = total_loads * GALLONS_PER_LOAD

    # Calculate the total cost of water for laundry in a year
    total_cost = total_gallons * COST_PER_GALLON

    # Display the total cost
    result = total_cost
    return result

print(solution())