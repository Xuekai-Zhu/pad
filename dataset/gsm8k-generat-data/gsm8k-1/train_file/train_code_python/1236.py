def solution():
    """Laura is hosting a carwash. She will charge $5 for a car, $6 for a truck, and $7 for an SUV. They raised $100 in total. If they washed 5 SUVs and 5 trucks, how many cars did they wash?"""
    suv_cost = 7
    truck_cost = 6
    car_cost = 5
    suv_count = 5
    truck_count = 5
    suv_total = suv_count * suv_cost
    truck_total = truck_count * truck_cost
    car_total = 100 - (suv_total + truck_total)
    car_count = car_total // car_cost
    result = car_count
    return result

print(solution())