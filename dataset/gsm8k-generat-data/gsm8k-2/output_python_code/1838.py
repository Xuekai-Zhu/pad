def solution():
    """John has a donkey and an elephant. The elephant weighs 3 tons (a ton is 2000 pounds). The donkey weighs 90% less. What is their combined weight in pounds?"""
    elephant_weight = 3 * 2000
    donkey_weight = 0.1 * elephant_weight
    total_weight = elephant_weight + donkey_weight
    result = total_weight
    return result

print(solution())