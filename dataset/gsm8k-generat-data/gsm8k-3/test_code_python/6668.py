def solution():
    """Winston had 10 gallons of gas in his car’s gas tank. He drives to the store and uses 6 gallons of gas. Then he drives to the doctor’s office and uses 2 gallons of gas. If the tank can hold up to 12 gallons of gas, how many gallons of gas will Winston need to refill the entire tank?"""
    # Define the initial amount of gas in the tank and the amount used on the trips
    initial_gas = 10
    trip_gas = 6 + 2

    # Define the maximum capacity of the gas tank
    max_capacity = 12

    # Calculate the amount of gas needed to refill the tank
    refill_gas = max_capacity - (initial_gas - trip_gas)

    # Display the amount of gas needed to refill the tank
    result = refill_gas
    return result

print(solution())