def solution():
    """Mason takes a bowl that holds 150 ml and fills it 2/3rds with oil and 1/3rd with vinegar. The oil weighs 5 g/ml and the vinegar weighs 4 g/ml. How many grams does the salad dressing weigh?"""
    # Define the volume of the bowl and the fractions of oil and vinegar used
    BOWL_VOLUME = 150
    OIL_FRACTION = 2/3
    VINEGAR_FRACTION = 1/3

    # Define the weight of oil and vinegar per ml
    OIL_WEIGHT = 5
    VINEGAR_WEIGHT = 4

    # Calculate the volume of oil and vinegar used
    oil_volume = BOWL_VOLUME * OIL_FRACTION
    vinegar_volume = BOWL_VOLUME * VINEGAR_FRACTION

    # Calculate the weight of the oil and the vinegar
    oil_weight = oil_volume * OIL_WEIGHT
    vinegar_weight = vinegar_volume * VINEGAR_WEIGHT

    # Calculate the total weight of the salad dressing
    total_weight = oil_weight + vinegar_weight

    # Display the total weight of the salad dressing
    result = total_weight
    return result

print(solution())