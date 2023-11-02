def solution():
    num_cars = 20
    num_passengers_per_car = 2
    num_additional_passengers = 1
    
    # Calculate the total number of passengers before the halfway point
    total_passengers = num_cars * (num_passengers_per_car + 1)
    
    # Calculate the number of additional passengers after the halfway point
    additional_passengers = num_cars * num_additional_passengers
    
    # Add the additional passengers to the total number of passengers
    total_passengers += additional_passengers
    
    result = total_passengers
    return result

print(solution())