def solution():
    """Donny went to the gas station to gas up his tank. He knows his truck holds 150 liters of fuel. His truck already contained 38 liters. How much change will he get from $350 if each liter of fuel costs $3?"""
    # Define the capacity and current amount of fuel in Donny's truck
    TRUCK_CAPACITY = 150
    current_amount = 38

    # Calculate the amount of fuel Donny needs to fill up his tank
    fuel_needed = TRUCK_CAPACITY - current_amount

    # Calculate the total cost of the fuel
    fuel_cost = fuel_needed * 3

    # Calculate the change Donny will get from $350
    change = 350 - fuel_cost

    # Display the change Donny will get
    result = change
    return result

print(solution())