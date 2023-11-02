def solution():
    # Let's assume the number of roosters is x
    # Then the number of hens is 9x - 5
    # And the total number of chickens is x + (9x - 5) = 10x - 5

    total_chickens = 75
    # 10x - 5 = 75
    # 10x = 80
    # x = 8
    roosters = 8
    hens = 9*8 - 5
    result = hens
    return result

print(solution())