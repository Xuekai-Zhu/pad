def solution():
    """Wendy's truck has a gas tank that can hold 20 gallons. She also has a car with a gas tank that holds 12 gallons. The truck's tank is half full. The car's tank is 1/3 full. If she fills them both up completely, how many gallons does she add?"""
    # Define the capacity of Wendy's truck and car gas tanks
    TRUCK_CAPACITY = 20
    CAR_CAPACITY = 12

    # Define the amount of gas currently in each tank
    truck_gas = TRUCK_CAPACITY / 2
    car_gas = CAR_CAPACITY / 3

    # Calculate the amount of gas needed to fill up each tank
    truck_gas_needed = TRUCK_CAPACITY - truck_gas
    car_gas_needed = CAR_CAPACITY - car_gas

    # Calculate the total amount of gas needed to fill up both tanks
    total_gas_needed = truck_gas_needed + car_gas_needed

    # Display the total amount of gas needed to fill up both tanks
    result = total_gas_needed
    return result

print(solution())