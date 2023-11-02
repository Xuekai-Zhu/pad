def solution():
    """John uses a 75-watt electric fan for 8 hours a day. How much kWh of electric energy does he consume per month (30 days) for using the electric fan?"""
    # Define the power of the electric fan in watts and the hours of use per day
    FAN_POWER = 75
    HOURS_PER_DAY = 8

    # Calculate the energy consumption per hour in kWh
    energy_per_hour = FAN_POWER / 1000  # convert from watts to kilowatts

    # Calculate the energy consumption per day in kWh
    energy_per_day = energy_per_hour * HOURS_PER_DAY

    # Calculate the energy consumption per month in kWh
    energy_per_month = energy_per_day * 30

    # Display the energy consumption per month
    result = energy_per_month
    return result

print(solution())