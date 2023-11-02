def solution():
    # Calculate the miles per gallon ratio
    miles_per_gallon = 400 / 20  # 20 gallons for 400 miles

    # Calculate the amount of gas needed for 600 miles
    gas_needed = (600 * 2) / miles_per_gallon  # Mr. Montero is going back and forth, so multiply by 2

    # Calculate how much more gas Mr. Montero needs
    additional_gas_needed = gas_needed - 8  # Mr. Montero's car already has 8 gallons of gas

    result = additional_gas_needed
    return result

print(solution())