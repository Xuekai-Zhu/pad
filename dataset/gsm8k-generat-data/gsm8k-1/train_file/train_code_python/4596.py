def solution():
    """Mason is mixing up some salad dressing. He takes a bowl that holds 150 ml and fills it 2/3rds with oil and 1/3rd with vinegar. The oil weighs 5 g/ml and the vinegar weighs 4 g/ml. How many grams does the salad dressing weigh?"""
    bowl_size = 150
    oil_ratio = 2/3
    vinegar_ratio = 1/3
    oil_weight = 5
    vinegar_weight = 4
    oil_amount = bowl_size * oil_ratio
    vinegar_amount = bowl_size * vinegar_ratio
    total_weight = (oil_amount * oil_weight) + (vinegar_amount * vinegar_weight)
    result = total_weight
    return result

print(solution())