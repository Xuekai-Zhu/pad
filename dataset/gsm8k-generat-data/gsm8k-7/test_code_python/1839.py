def solution():
    # Convert elephant weight to pounds
    elephant_weight = 3 * 2000

    # Calculate donkey weight as 90% less than elephant weight
    donkey_weight = 0.1 * elephant_weight

    # Calculate combined weight in pounds
    combined_weight = elephant_weight + donkey_weight

    result = combined_weight
    return result

print(solution())