def solution():
    """John uses a 75-watt electric fan for 8 hours a day. How much kWh of electric energy does he consume per month (30 days) for using the electric fan?"""
    # Define the power consumption in watts
    power = 75

    # Define the hours of use per day
    hours_per_day = 8

    # Calculate the energy consumption in watt-hours per day
    energy_per_day = power * hours_per_day

    # Convert the energy consumption to kilowatt-hours per day
    energy_per_day_kwh = energy_per_day / 1000

    # Calculate the energy consumption per month
    energy_per_month_kwh = energy_per_day_kwh * 30

    # return the result
    result = energy_per_month_kwh
    return result

print(solution())