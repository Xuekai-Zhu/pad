def solution():
    """4.5 gallons of coffee were divided among 18 thermoses. Genevieve drank 3 thermoses. How many pints of coffee did Genevieve drink?"""
    gallons_per_thermos = 4.5 / 18
    pints_per_gallon = 8
    pints_drank = 3 * gallons_per_thermos * pints_per_gallon
    result = pints_drank
    return result

print(solution())