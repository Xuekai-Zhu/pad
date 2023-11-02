def solution():
    # Convert 20 gallons to pints
    total_pints = 20 * 8 * 4

    # Calculate the number of pints in each container
    pints_per_container = total_pints / 80

    # Calculate the number of pints that Geraldo drank
    gerardo_drank = 3.5 * pints_per_container
    result = gerardo_drank
    return result

print(solution())