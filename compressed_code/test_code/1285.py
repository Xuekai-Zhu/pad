def solution():
    
    rose_share = 1800
    purity_share = rose_share / 3
    sheila_share = 5 * purity_share
    total_rent = rose_share + purity_share + sheila_share
    result = total_rent
    return result

print(solution())