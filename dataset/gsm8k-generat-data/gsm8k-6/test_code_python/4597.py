def solution():
    # Calculate the volume of oil and vinegar in the bowl
    oil_volume = (2/3) * 150
    vinegar_volume = (1/3) * 150

    # Calculate the weight of the oil and vinegar
    oil_weight = oil_volume * 5
    vinegar_weight = vinegar_volume * 4

    # Calculate the total weight of the salad dressing
    total_weight = oil_weight + vinegar_weight
    result = total_weight
    return result

print(solution())