def solution():
    # Calculate the amount of fuel Donny needs to fill his tank
    fuel_needed = 150 - 38

    # Calculate the cost of the fuel Donny needs
    fuel_cost = fuel_needed * 3

    # Calculate the change Donny will receive
    change = 350 - fuel_cost

    result = change
    return result

print(solution())