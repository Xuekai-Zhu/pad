def solution():
    bowl_volume = 150  # The bowl holds 150 ml of salad dressing
    oil_ratio = 2 / 3  # 2/3 of the bowl is filled with oil
    vinegar_ratio = 1 / 3  # 1/3 of the bowl is filled with vinegar
    oil_density = 5  # The density of oil is 5 g/ml
    vinegar_density = 4  # The density of vinegar is 4 g/ml

    # Calculate the volume of oil and vinegar in the bowl
    oil_volume = bowl_volume * oil_ratio
    vinegar_volume = bowl_volume * vinegar_ratio

    # Calculate the weight of oil and vinegar in the bowl
    oil_weight = oil_volume * oil_density
    vinegar_weight = vinegar_volume * vinegar_density

    # Calculate the total weight of the salad dressing
    total_weight = oil_weight + vinegar_weight
    result = total_weight
    return result

print(solution())