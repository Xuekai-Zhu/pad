def solution():
    """A bag of flour is divided into 8 portions of 2 kilograms each. How much flour (in kilograms) was in three bags in total, before it was divided into portions?"""
    portions_per_bag = 8
    weight_per_portion = 2
    bags = 3
    total_weight = portions_per_bag * weight_per_portion * bags
    result = total_weight
    return result

print(solution())