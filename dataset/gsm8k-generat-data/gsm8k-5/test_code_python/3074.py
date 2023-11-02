def solution():
    # Calculate the total number of M&Ms after Carter eats some and his sister adds some
    total_MMs = 20 + 20 - 12 + (20/2) + 14  # 20 green M&Ms, 20 red M&Ms, subtract 12 green, half of the remaining red, add 14 yellow

    # Calculate the probability of picking a green M&M
    green_MMs = 20 - 12  # Carter starts with 20 green M&Ms, but eats 12
    probability = green_MMs / total_MMs * 100

    result = probability
    return result

print(solution())