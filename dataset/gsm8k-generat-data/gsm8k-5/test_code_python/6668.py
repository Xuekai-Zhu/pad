def solution():
    starting_gas = 10 # Winston had 10 gallons of gas in his car’s gas tank
    drove_to_store = 6 # he drives to the store and uses 6 gallons of gas
    drove_to_doctors = 2 # then he drives to the doctor’s office and uses 2 gallons of gas
    tank_capacity = 12 # the tank can hold up to 12 gallons of gas

    # Calculate the remaining gas in the tank
    remaining_gas = starting_gas - drove_to_store - drove_to_doctors

    # Calculate the amount of gas needed to refill the tank
    gas_needed = tank_capacity - remaining_gas
    result = gas_needed
    return result

print(solution())