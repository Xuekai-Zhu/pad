def solution():
    water_liters = 20
    vinegar_liters = 18

    # Calculate the amount of water and vinegar used in the mixture
    water_in_mixture = water_liters * (3/5)
    vinegar_in_mixture = vinegar_liters * (5/6)

    # Calculate the total volume of the mixture
    total_mixture_volume = water_in_mixture + vinegar_in_mixture
    result = total_mixture_volume
    return result

print(solution())