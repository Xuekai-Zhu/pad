def solution():
    wattage = 75  # The electric fan has a wattage of 75 watts
    hours_per_day = 8  # John uses the fan for 8 hours per day
    days_per_month = 30  # There are 30 days in a month

    # Calculate the total energy consumed by the electric fan in a month
    total_energy = (wattage * hours_per_day * days_per_month) / 1000  # Convert watt-hours to kilowatt-hours (kWh)

    result = total_energy
    return result

print(solution())