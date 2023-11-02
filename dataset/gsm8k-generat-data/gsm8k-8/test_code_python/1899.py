def solution():
    # Define the ratios of grape to cherry and grape to apple candies
    grape_to_cherry_ratio = 3
    grape_to_apple_ratio = 2

    # Calculate the total ratio of grape, cherry, and apple candies
    total_ratio = grape_to_cherry_ratio + 1 + grape_to_apple_ratio

    # Calculate the cost per candy
    cost_per_candy = 2.5

    # Calculate the total number of candies
    total_cost = 200
    total_candies = total_cost / cost_per_candy

    # Calculate the number of grape candies
    grape_candies = (grape_to_cherry_ratio / total_ratio) * total_candies
    result = grape_candies
    return result

print(solution())