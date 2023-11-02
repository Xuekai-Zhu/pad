def solution():
    # Calculate how much gas Winston used in total
    used_gas = 6 + 2  # Winston used 6 gallons of gas to drive to the store and 2 gallons to drive to the doctor's office

    # Calculate how much gas is left in the tank
    remaining_gas = 10 - used_gas  # Winston started with 10 gallons of gas and used 8 gallons in total

    # Calculate how much gas Winston needs to refill the tank
    refill_gas = 12 - remaining_gas  # the tank can hold up to 12 gallons of gas, so Winston needs to add the difference between how much gas is left and how much the tank can hold

    result = refill_gas
    return result

print(solution())