def solution():
    # Define the capacity of Donny's truck and the amount already in it
    truck_capacity = 150
    current_amount = 38

    # Calculate the amount of fuel Donny needs to fill up the tank
    fuel_needed = truck_capacity - current_amount

    # Calculate the cost of the fuel Donny needs to buy
    fuel_cost = fuel_needed * 3
    
    # Calculate the change Donny will receive after paying with $350
    change = 350 - fuel_cost

    result = change
    return result

print(solution())