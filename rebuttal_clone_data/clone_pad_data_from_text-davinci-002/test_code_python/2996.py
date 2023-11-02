def solution():
    consumption_rate = 4
    miles_today = 400
    extra_miles_tomorrow = 200
    total_miles = miles_today + extra_miles_tomorrow
    total_gas = total_miles * consumption_rate
    result = total_gas
    return result

print(solution())