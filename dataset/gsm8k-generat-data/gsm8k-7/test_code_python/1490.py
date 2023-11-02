def solution():
    total_weight = 10
    apple_weight = 3
    orange_weight = 1
    grape_weight = 3

    # Calculate the total weight of fruits other than strawberries
    other_fruits_weight = apple_weight + orange_weight + grape_weight

    # Calculate the weight of strawberries
    strawberry_weight = total_weight - other_fruits_weight
    result = strawberry_weight
    return result

print(solution())