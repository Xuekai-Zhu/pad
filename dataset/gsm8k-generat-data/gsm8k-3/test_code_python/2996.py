def solution():
    """Dream's car consumes 4 gallons of gas per mile. If she drives 400 miles today and 200 more miles tomorrow than today, how many gallons of gas will the car consume?"""
    # Define the gas consumption rate per mile
    GAS_CONSUMPTION_RATE = 4

    # Calculate the total miles driven
    total_miles = 400 + 200

    # Calculate the total gallons of gas consumed
    gallons_of_gas = total_miles * GAS_CONSUMPTION_RATE

    # Display the total gallons of gas consumed
    result = gallons_of_gas
    return result

print(solution())