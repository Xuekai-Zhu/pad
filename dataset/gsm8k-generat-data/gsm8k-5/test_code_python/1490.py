def solution():
    total_weight = 10  # Tommy ordered a total weight of 10 kilograms of fruits
    apples_weight = 3  # Tommy ordered 3 kilograms of apples
    orange_weight = 1  # Tommy ordered 1 kilogram of orange
    grapes_weight = 3  # Tommy ordered 3 kilograms of grapes

    # Calculate the weight of strawberries Tommy ordered
    strawberries_weight = total_weight - (apples_weight + orange_weight + grapes_weight)
    result = strawberries_weight
    return result

print(solution())