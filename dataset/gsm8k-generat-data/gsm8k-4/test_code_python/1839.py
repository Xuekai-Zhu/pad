def solution():
    """John has a donkey and an elephant. The elephant weighs 3 tons (a ton is 2000 pounds). The donkey weighs 90% less. What is their combined weight in pounds?"""
    # Define the weight of the elephant in pounds
    elephant_weight = 3 * 2000

    # Calculate the weight of the donkey, which is 90% less than the weight of the elephant
    donkey_weight = elephant_weight * 0.1

    # Calculate the total weight of the two animals
    total_weight = elephant_weight + donkey_weight

    result = total_weight
    return result

print(solution())