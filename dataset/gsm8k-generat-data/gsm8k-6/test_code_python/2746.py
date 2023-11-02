def solution():
    # Find the weight of Al
    weight_A = 146 + 38  # Ed weighs 146 pounds and is 38 pounds lighter than Al
    # Find the weight of Ben
    weight_B = weight_A - 25  # Al is 25 pounds heavier than Ben
    # Find the weight of Carl
    weight_C = weight_B + 16  # Ben is 16 pounds lighter than Carl
    result = weight_C
    return result

print(solution())