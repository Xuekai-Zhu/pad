def solution():
    """Dream's car consumes 4 gallons of gas per mile. If she drives 400 miles today and 200 more miles tomorrow than today, how many gallons of gas will the car consume?"""
    # Define the gas consumption rate
    gas_consumption_rate = 4

    # Calculate the total distance traveled
    total_distance = 400 + 600  # 400 miles today + 200 more miles tomorrow

    # Calculate the total gas consumption
    gas_consumption = total_distance * gas_consumption_rate

    # Return the result
    result = gas_consumption
    return result

print(solution())