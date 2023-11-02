def solution():
    """Daniel has 5 jars of juice containing 2 liters each. He wants to serve a full glass of juice to each person at a party. He knows that each glass can hold up to 250 milliliters of juice. How many full glasses can he give?"""
    liters_per_jar = 2
    num_jars = 5
    ml_per_glass = 250
    total_ml = liters_per_jar * num_jars * 1000
    num_glasses = total_ml // ml_per_glass
    result = num_glasses
    return result

print(solution())