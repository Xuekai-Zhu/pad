def solution():
    """Kim's TV uses 125 watts of electricity per hour.  She runs it for 4 hours a day.  If electricity cost 14 cents per kw/h how many cents does her TV cost to run for a week?"""
    # Define the power consumption of the TV in watts and the hours it is on per day
    POWER_CONSUMPTION = 125
    HOURS_PER_DAY = 4

    # Calculate the daily energy consumption in kilowatt-hours (kWh)
    energy_consumption = (POWER_CONSUMPTION * HOURS_PER_DAY) / 1000

    # Calculate the weekly energy consumption in kilowatt-hours (kWh)
    weekly_energy_consumption = energy_consumption * 7

    # Calculate the cost of the energy consumption in cents
    COST_PER_KWH = 14
    cost = weekly_energy_consumption * COST_PER_KWH

    # Display the cost in cents
    result = cost
    return result

print(solution())