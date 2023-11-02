def solution():
    suv_count = 5
    truck_count = 5
    car_price = 5
    truck_price = 6
    suv_price = 7
    total_raised = 100

    # Calculate the total amount raised from washing SUVs and trucks
    suv_total = suv_count * suv_price
    truck_total = truck_count * truck_price
    car_total = total_raised - suv_total - truck_total

    # Calculate the number of cars washed
    car_count = car_total / car_price
    result = car_count
    return result

print(solution())