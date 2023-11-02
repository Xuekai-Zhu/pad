def solution():
    """Winston had 10 gallons of gas in his car’s gas tank. He drives to the store and uses 6 gallons of gas. 
    Then he drives to the doctor’s office and uses 2 gallons of gas. If the tank can hold up to 12 gallons of gas, 
    how many gallons of gas will Winston need to refill the entire tank?"""
    starting_gas = 10
    store_gas = 6
    doctor_gas = 2
    max_gas = 12
    remaining_gas = max_gas - (starting_gas - store_gas - doctor_gas)
    result = remaining_gas
    return result

print(solution())