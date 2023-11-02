def solution():
    """Mason is mixing up some salad dressing. He takes a bowl that holds 150 ml and fills it 2/3rds with oil and 1/3rd with vinegar. The oil weighs 5 g/ml and the vinegar weighs 4 g/ml. How many grams does the salad dressing weigh?"""
    # Define the volume of the bowl and the proportions of oil and vinegar
    bowl_volume = 150
    oil_proportion = 2/3
    vinegar_proportion = 1/3

    # Calculate the volumes of oil and vinegar
    oil_volume = bowl_volume * oil_proportion
    vinegar_volume = bowl_volume * vinegar_proportion

    # Calculate the weights of oil and vinegar
    oil_weight = oil_volume * 5
    vinegar_weight = vinegar_volume * 4

    # Calculate the total weight of the salad dressing
    total_weight = oil_weight + vinegar_weight

    result = total_weight
    return result

print(solution())