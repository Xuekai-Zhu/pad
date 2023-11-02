def solution():
    # Calculate the weight of strawberries Tommy ordered
    total_weight = 10  # total weight of fruits ordered
    apples_weight = 3  # weight of apples ordered
    orange_weight = 1  # weight of orange ordered
    grapes_weight = 3  # weight of grapes ordered
    strawberries_weight = total_weight - (apples_weight + orange_weight + grapes_weight)  # weight of strawberries ordered
    result = strawberries_weight
    return result

print(solution())