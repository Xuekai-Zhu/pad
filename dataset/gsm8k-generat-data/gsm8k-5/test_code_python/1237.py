def solution():
    suv_price = 7
    truck_price = 6
    car_price = 5
    
    suv_count = 5
    truck_count = 5
    
    total_raised = 100
    total_count = suv_count + truck_count + car_count
    
    # Set up a system of equations to solve for the number of cars washed
    # 5suv_count * suv_price + 5truck_count * truck_price + car_count * car_price = total_raised
    # suv_count + truck_count + car_count = total_count
    
    # Substitute the second equation into the first
    # 5suv_count * suv_price + 5truck_count * truck_price + (total_count - suv_count - truck_count) * car_price = total_raised
    
    # Simplify and solve for car_count
    car_count = (total_raised - 5*suv_price - 5*truck_price) / (car_price - 1)
    
    result = car_count
    return result

print(solution())