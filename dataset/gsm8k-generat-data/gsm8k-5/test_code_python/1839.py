def solution():
    elephant_weight = 3 * 2000  # The elephant weighs 3 tons (2000 pounds per ton)
    donkey_weight = elephant_weight * 0.1  # The donkey weighs 90% less than the elephant
    total_weight = elephant_weight + donkey_weight  # Calculate the total weight in pounds
    result = total_weight
    return result

print(solution())