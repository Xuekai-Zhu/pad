def solution():
    # Calculate how many gallons are already in each tank
    truck_gallons = 20/2  # the truck's tank is half full
    car_gallons = 12/3  # the car's tank is 1/3 full

    # Calculate how many gallons Wendy needs to add to fill up both tanks completely
    total_gallons = 20 - truck_gallons + 12 - car_gallons

    result = total_gallons
    return result

print(solution())