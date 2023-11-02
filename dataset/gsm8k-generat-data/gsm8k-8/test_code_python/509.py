def solution():
    # Define the electricity price per kilowatt-hour
    price_per_kwh = 0.10
    
    # Define the oven's consumption rate in kilowatt-hours
    consumption_rate = 2.4
    
    # Define the total hours the oven was used
    total_hours = 25
    
    # Calculate the total consumption in kilowatt-hours
    total_consumption = consumption_rate * total_hours
    
    # Calculate the total cost
    total_cost = total_consumption * price_per_kwh
    
    result = total_cost
    return result

print(solution())