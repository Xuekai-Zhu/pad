def solution():
    total_weight = 439
    pitbull_weight = 3 * chihuahua_weight
    great_dane_weight = pitbull_weight * 3 + 10
    chihuahua_weight = total_weight - (pitbull_weight + great_dane_weight)
    result = great_dane_weight
    return result

print(solution())