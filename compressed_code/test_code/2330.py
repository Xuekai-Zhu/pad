def solution():
    
    gas_per_mile = 4
    today_miles = 400
    tomorrow_miles = today_miles + 200
    total_miles = today_miles + tomorrow_miles
    total_gas = gas_per_mile * total_miles
    result = total_gas
    return result

print(solution())