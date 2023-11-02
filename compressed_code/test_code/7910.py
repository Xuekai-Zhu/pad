def solution():
    
    watt_hours_per_day = 75 * 8
    watt_hours_per_month = watt_hours_per_day * 30
    kilowatt_hours = watt_hours_per_month / 1000
    result = kilowatt_hours
    return result

print(solution())