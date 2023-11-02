def solution():
    miles_today = 400
    miles_tomorrow = miles_today + 200
    gas_per_mile = 4

    # Calculate the total gallons of gas consumed on both days
    total_gas = (miles_today + miles_tomorrow) * gas_per_mile

    result = total_gas
    return result

print(solution())