def solution():
    """John has a donkey and an elephant.  The elephant weighs 3 tons (a ton is 2000 pounds).  The donkey weighs 90% less.  What is their combined weight in pounds?"""
    # Convert the weight of the elephant from tons to pounds
    elephant_weight = 3 * 2000

    # Calculate the weight of the donkey
    donkey_weight = 0.1 * elephant_weight

    # Calculate the total weight of the animals in pounds
    total_weight = elephant_weight + donkey_weight

    result = total_weight
    return result

print(solution())