def solution():
    # Define the total weight of all fruits and the weight of each fruit that Tommy ordered
    total_weight = 10
    apple_weight = 3
    orange_weight = 1
    grape_weight = 3

    # Calculate the weight of strawberries Tommy ordered
    strawberry_weight = total_weight - (apple_weight + orange_weight + grape_weight)
    result = strawberry_weight
    return result

print(solution())