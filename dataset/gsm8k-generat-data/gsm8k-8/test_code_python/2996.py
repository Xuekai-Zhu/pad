def solution():
    # Define the variables
    miles_today = 400
    miles_tomorrow = miles_today + 200
    gas_per_mile = 4

    # Calculate the total gallons of gas consumed
    total_gallons = gas_per_mile * (miles_today + miles_tomorrow)

    result = total_gallons
    return result

print(solution())