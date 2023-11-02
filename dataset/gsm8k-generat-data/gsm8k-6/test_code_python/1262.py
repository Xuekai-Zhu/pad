def solution():
    total_gallons = 4.5  # gallons of coffee
    total_pints = total_gallons * 8  # convert to pints
    thermoses = 18  # number of thermoses
    pints_per_thermos = total_pints / thermoses  # pints of coffee per thermos
    genevieve_thermos = 3  # number of thermoses Genevieve drank
    genevieve_pints = genevieve_thermos * pints_per_thermos  # pints of coffee Genevieve drank
    result = genevieve_pints
    return result

print(solution())