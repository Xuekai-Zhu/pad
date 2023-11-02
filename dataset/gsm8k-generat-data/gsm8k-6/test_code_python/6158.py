def solution():
    # Calculate the amount paid for the power used by the water heater
    water_heater = 500 / 2

    # Calculate the amount paid for the power used by the refrigerator
    refrigerator = 3 * water_heater

    # Calculate the total amount paid for the power used by all gadgets
    total = refrigerator + water_heater + 500

    result = total
    return result

print(solution())