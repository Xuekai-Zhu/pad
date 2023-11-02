def solution():
    """Mason is mixing up some salad dressing. He takes a bowl that holds 150 ml and fills it 2/3rds with oil and 1/3rd with vinegar. The oil weighs 5 g/ml and the vinegar weighs 4 g/ml. How many grams does the salad dressing weigh?"""
    bowl_size = 150
    oil_proportion = 2/3
    vinegar_proportion = 1/3
    oil_density = 5
    vinegar_density = 4
    oil_volume = bowl_size * oil_proportion
    vinegar_volume = bowl_size * vinegar_proportion
    total_weight = (oil_volume * oil_density) + (vinegar_volume * vinegar_density)
    result = total_weight
    return result

print(solution())