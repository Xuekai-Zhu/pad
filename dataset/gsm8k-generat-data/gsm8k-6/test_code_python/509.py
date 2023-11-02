def solution():
    electricity_price = 0.10  # price per kWh
    consumption_rate = 2.4  # kWh consumed per hour
    usage_time = 25  # hours of usage
    total_consumption = consumption_rate * usage_time
    total_cost = electricity_price * total_consumption
    result = round(total_cost, 2)
    return result

print(solution())