def solution():
    # Calculate the total number of flowers after the fungus
    total_flowers = (125 - 45) + (125 - 61) + (125 - 30) + (125 - 40)

    # Calculate the number of bouquets the florist can make
    bouquets = total_flowers // 9
    result = bouquets
    return result

print(solution())