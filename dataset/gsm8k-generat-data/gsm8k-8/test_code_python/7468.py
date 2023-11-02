def solution():
    # Define the total cost and base price
    total_cost = 23
    base_price = 3
    
    # Calculate the cost of the mileage
    mileage_cost = total_cost - base_price
    
    # Calculate the distance traveled
    distance_traveled = mileage_cost / 4
    
    result = distance_traveled
    return result

print(solution())