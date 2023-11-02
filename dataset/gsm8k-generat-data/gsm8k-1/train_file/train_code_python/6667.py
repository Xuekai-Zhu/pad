def solution():
    """Winston had 10 gallons of gas in his car’s gas tank. He drives to the store and uses 6 gallons of gas.
    Then he drives to the doctor’s office and uses 2 gallons of gas.
    If the tank can hold up to 12 gallons of gas, how many gallons of gas will Winston need to refill the entire tank?"""
    starting_gas = 10
    gas_used_store = 6
    gas_used_doctor = 2
    tank_capacity = 12
    remaining_gas = starting_gas - gas_used_store - gas_used_doctor
    refill_amount = tank_capacity - remaining_gas
    result = refill_amount
    return result

print(solution())