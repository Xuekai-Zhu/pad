def solution():
    """John uses a 75-watt electric fan for 8 hours a day. How much kWh of electric energy does he consume per month (30 days) for using the electric fan?"""
    watt_hours_per_day = 75 * 8
    watt_hours_per_month = watt_hours_per_day * 30
    kilowatt_hours = watt_hours_per_month / 1000
    result = kilowatt_hours
    return result

print(solution())