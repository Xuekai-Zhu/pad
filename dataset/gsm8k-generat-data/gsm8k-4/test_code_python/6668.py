def solution():
    """Winston had 10 gallons of gas in his car’s gas tank. He drives to the store and uses 6 gallons of gas. 
    Then he drives to the doctor’s office and uses 2 gallons of gas. If the tank can hold up to 12 gallons of gas, 
    how many gallons of gas will Winston need to refill the entire tank?"""
    
    # Define the initial amount of gas in Winston's car
    initial_gas = 10

    # Define the amount of gas used while driving to the store and the doctor's office
    used_gas = 6 + 2

    # Define the capacity of the gas tank
    gas_capacity = 12

    # Calculate how many gallons of gas Winston will need to refill the entire tank
    refill_gas = gas_capacity - (initial_gas - used_gas)

    # Return the result
    result = refill_gas
    return result

print(solution())