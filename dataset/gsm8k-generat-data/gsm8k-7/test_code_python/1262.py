def solution():
    total_gallons = 4.5
    num_thermoses = 18
    num_drunk = 3
    # Calculate the total number of pints
    total_pints = total_gallons * 8

    # Calculate the number of pints in each thermos
    pints_per_thermos = total_pints / num_thermoses

    # Calculate the total number of pints that Genevieve drank
    total_drunk = num_drunk * pints_per_thermos

    result = total_drunk
    return result

print(solution())