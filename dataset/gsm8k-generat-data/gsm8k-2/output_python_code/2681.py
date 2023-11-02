def solution():
    """John uses a 75-watt electric fan for 8 hours a day. How much kWh of electric energy does he consume per month (30 days) for using the electric fan?"""
    fan_power = 75/1000 # converting watts to kilowatts
    daily_energy_consumption = fan_power * 8 # in kWh
    monthly_energy_consumption = daily_energy_consumption * 30
    result = monthly_energy_consumption
    return result

print(solution())