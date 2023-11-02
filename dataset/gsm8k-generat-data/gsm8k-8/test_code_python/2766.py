def solution():
    total_stems = 52
    mom = 15
    grandma = mom + 6
    leftover = total_stems - mom - grandma
    result = leftover
    return result

print(solution())