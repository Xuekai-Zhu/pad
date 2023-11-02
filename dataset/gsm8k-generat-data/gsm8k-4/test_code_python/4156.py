def solution():
    """Wendy's truck has a gas tank that can hold 20 gallons. She also has a car with a gas tank that holds 12 gallons. The truck's tank is half full. The car's tank is 1/3 full. If she fills them both up completely, how many gallons does she add?"""
    # Define the maximum capacity of the gas tanks
    truck_capacity = 20
    car_capacity = 12

    # Calculate the current amount of gas in the tanks
    truck_current = truck_capacity / 2
    car_current = car_capacity / 3

    # Calculate the amount of gas needed to fill up each tank
    truck_fill = truck_capacity - truck_current
    car_fill = car_capacity - car_current

    # Calculate the total amount of gas needed to fill up both tanks
    total_fill = truck_fill + car_fill

    # return the result
    result = total_fill
    return result

print(solution())