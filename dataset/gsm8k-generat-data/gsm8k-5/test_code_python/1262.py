def solution():
    total_gallons = 4.5  # 4.5 gallons of coffee were divided among 18 thermoses
    thermoses_drunk = 3  # Genevieve drank 3 thermoses

    # Calculate the total pints of coffee
    total_pints = total_gallons * 8  # 1 gallon = 8 pints

    # Calculate the pints of coffee Genevieve drank
    genevieve_pints = (total_gallons / 18) * 3 * 8  # Genevieve drank 3 thermoses out of 18, each thermos holds 1/18 of total gallons

    result = genevieve_pints
    return result

print(solution())