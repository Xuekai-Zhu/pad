def solution():
    elephant_weight = 3 * 2000  # the weight of the elephant in pounds
    donkey_weight = 0.1 * elephant_weight  # the weight of the donkey is 90% less than the weight of the elephant
    combined_weight = elephant_weight + donkey_weight  # the total combined weight of the animals
    result = combined_weight
    return result

print(solution())