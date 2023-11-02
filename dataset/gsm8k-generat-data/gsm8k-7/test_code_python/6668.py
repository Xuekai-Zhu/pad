def solution():
    starting_gallons = 10
    drive_to_store = 6
    drive_to_doctor = 2
    tank_capacity = 12

    # Calculate the total amount of gas used
    total_gas_used = drive_to_store + drive_to_doctor

    # Calculate the current amount of gas in the tank
    current_gas = starting_gallons - total_gas_used

    # Calculate the amount of gas needed to fill the tank
    gas_needed = tank_capacity - current_gas
    result = gas_needed
    return result

print(solution())