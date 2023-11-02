def solution():
    fan_wattage = 75
    daily_usage_hours = 8
    days_per_month = 30

    # Calculate the daily energy consumption in kWh
    daily_energy_consumption = (fan_wattage * daily_usage_hours) / 1000

    # Calculate the total energy consumption in kWh for the entire month
    monthly_energy_consumption = daily_energy_consumption * days_per_month

    result = monthly_energy_consumption
    return result

print(solution())