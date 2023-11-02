def solution():
    # Define the prices of each vehicle
    car_price = 5
    truck_price = 6
    suv_price = 7

    # Define the number of SUVs and trucks that were washed
    num_suv = 5
    num_truck = 5

    # Calculate the total amount raised
    total_raised = (num_suv * suv_price) + (num_truck * truck_price)

    # Calculate the number of cars washed
    num_car = (100 - total_raised) / car_price
    result = num_car
    return result

print(solution())