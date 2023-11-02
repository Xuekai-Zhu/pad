def solution():
    
    fan_power = 75/1000 
    daily_energy_consumption = fan_power * 8 
    monthly_energy_consumption = daily_energy_consumption * 30
    result = monthly_energy_consumption
    return result

print(solution())