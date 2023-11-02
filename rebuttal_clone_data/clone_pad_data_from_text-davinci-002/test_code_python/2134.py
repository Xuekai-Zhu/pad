def solution():
    Martha_cans = 90
    Diego_cans = Martha_cans / 2 + 10
    total_cans = Diego_cans + Martha_cans
    cans_needed = 150 - total_cans
    result = cans_needed
    return result

print(solution())