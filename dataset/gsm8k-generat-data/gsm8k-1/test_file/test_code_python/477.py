def solution():
    """Belen has two kinds of pennies, a 2010 penny and a 1959 penny. The 2010 penny is three-quarters of the weight of the 1959 penny. If the 1959 penny weighs 48 grains, what is the combined weight of the two pennies?"""
    weight_1959_penny = 48
    weight_2010_penny = weight_1959_penny * (3/4)
    combined_weight = weight_1959_penny + weight_2010_penny
    result = combined_weight
    return result

print(solution())