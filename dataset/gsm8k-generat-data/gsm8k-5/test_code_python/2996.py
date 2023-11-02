def solution():
    gas_consumption = 4  # Dream's car consumes 4 gallons of gas per mile
    distance_today = 400  # Dream drives 400 miles today
    distance_tomorrow = 400 + 200  # Dream drives 200 more miles tomorrow than today

    # Calculate the total gas consumption for both days
    total_gas_consumption = gas_consumption * (distance_today + distance_tomorrow)

    result = total_gas_consumption
    return result

print(solution())