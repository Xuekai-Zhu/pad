def solution():
    """Daniel has 5 jars of juice containing 2 liters each. He wants to serve a full glass of juice to each person at a party. He knows that each glass can hold up to 250 milliliters of juice. How many full glasses can he give?"""
    jar_size_liters = 2
    num_jars = 5
    glass_size_ml = 250
    total_juice_ml = jar_size_liters * 1000 * num_jars
    total_glasses = total_juice_ml // glass_size_ml
    result = total_glasses
    return result

print(solution())