def solution():
    wattage = 75
    hours_used = 8
    days_in_month = 30
    hours_in_day = 24
    total_hours = hours_used * days_in_month
    total_kilowatts = total_hours * (wattage / 1000)
    result = total_kilowatts
    return result

print(solution())