def solution():
    # Calculate the energy consumption for one day in kWh
    daily_energy_consumption = (75 / 1000) * 8

    # Calculate the monthly energy consumption in kWh
    monthly_energy_consumption = daily_energy_consumption * 30

    result = monthly_energy_consumption
    return result

print(solution())