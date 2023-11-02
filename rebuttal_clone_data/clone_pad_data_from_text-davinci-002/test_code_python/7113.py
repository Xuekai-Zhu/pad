def solution():
    bucket1 = 11
    bucket2 = 13
    bucket3 = 12
    bucket4 = 16
    bucket5 = 10
    total1 = bucket1 + bucket2 + bucket3 + bucket4 + bucket5
    total2 = total1 - bucket5
    bucket6 = bucket5 + bucket4
    total3 = total2 - bucket6
    result = total3
    return result

print(solution())