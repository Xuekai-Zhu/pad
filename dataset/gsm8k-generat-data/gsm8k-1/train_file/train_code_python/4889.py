def solution():
    """Before Marcus went on a road trip to LA, his car had 1728 miles on it. He filled his empty gas tank twice and used up all the gas on the trip. If Marcus's car gets 30 miles per gallon and holds 20 gallons of gas, how many miles does Marcus' car have on it now?"""
    initial_miles = 1728
    gas_capacity = 20
    miles_per_gallon = 30
    total_gas_used = gas_capacity * 2
    total_miles_driven = total_gas_used * miles_per_gallon
    final_miles = initial_miles + total_miles_driven
    result = final_miles
    return result

print(solution())