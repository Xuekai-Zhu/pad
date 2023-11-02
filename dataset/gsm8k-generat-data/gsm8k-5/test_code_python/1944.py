def solution():
    total_cans = 85  # Total number of collected cans
    ladonna_cans = 25  # Number of cans picked up by LaDonna
    prikya_cans = ladonna_cans * 2  # Number of cans picked up by Prikya, twice as much as LaDonna
    yoki_cans = total_cans - ladonna_cans - prikya_cans  # Number of cans picked up by Yoki, the rest

    result = yoki_cans
    return result

print(solution())