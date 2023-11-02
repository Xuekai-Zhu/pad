def solution():
    # Define the volume of the bowl and the ratios of oil and vinegar
    bowl_volume = 150
    oil_ratio = 2/3
    vinegar_ratio = 1/3

    # Calculate the volume of oil and vinegar
    oil_volume = bowl_volume * oil_ratio
    vinegar_volume = bowl_volume * vinegar_ratio

    # Calculate the weight of the oil and vinegar
    oil_weight = oil_volume * 5
    vinegar_weight = vinegar_volume * 4

    # Calculate the total weight of the salad dressing
    total_weight = oil_weight + vinegar_weight
    result = total_weight
    return result

print(solution())