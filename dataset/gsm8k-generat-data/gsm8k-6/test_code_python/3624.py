def solution():
    # Calculate the amount of gas needed to travel 90 miles
    gas_needed = 90 / 3  # the truck goes 3 miles per gallon
    gas_needed -= 12  # the truck already has 12 gallons of gas in the tank
    result = gas_needed
    return result

print(solution())