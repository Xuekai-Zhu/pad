def solution():
    
    suv_price = 7
    truck_price = 6
    car_price = 5
    total_cash = 100
    suv_count = 5
    truck_count = 5
    suv_cash = suv_count * suv_price
    truck_cash = truck_count * truck_price
    car_cash = total_cash - suv_cash - truck_cash
    car_count = car_cash / car_price
    result = car_count
    return result

print(solution())