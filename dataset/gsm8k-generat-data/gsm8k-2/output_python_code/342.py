def solution():
    """Kim's TV uses 125 watts of electricity per hour. She runs it for 4 hours a day. If electricity cost 14 cents per kw/h how many cents does her TV cost to run for a week?"""
    wattage = 125
    daily_hours = 4
    daily_energy_usage = wattage * daily_hours / 1000  # convert to kilowatt hours (kWh)
    weekly_energy_usage = daily_energy_usage * 7
    electricity_cost_per_kWh = 0.14
    total_cost = weekly_energy_usage * electricity_cost_per_kWh * 100  # convert to cents
    result = total_cost
    return result

print(solution())