def solution():
    # Calculate the total number of gallons needed to fill all 4 barrels
    total_gallons = 4 * 7  # Each barrel is 7 gallons.

    # Calculate the time it takes to fill all 4 barrels
    time_in_minutes = total_gallons / 3.5  # The faucet can fill 3.5 gallons per minute.
    result = time_in_minutes
    return result

print(solution())