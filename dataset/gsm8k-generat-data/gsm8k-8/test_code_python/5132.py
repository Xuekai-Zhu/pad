def solution():
    # Define the cost of each service
    oil_change_cost = 20
    repair_cost = 30
    car_wash_cost = 5
    
    # Define the number of cars that received each service
    oil_changes = 5
    repairs = 10
    car_washes = 15
    
    # Calculate the total earnings
    total_earnings = oil_change_cost * oil_changes + repair_cost * repairs + car_wash_cost * car_washes
    result = total_earnings
    return result

print(solution())