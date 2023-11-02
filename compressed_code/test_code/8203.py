def solution():
    
    beef = 10
    noodles_per_beef = 2
    noodles_already_have = 4
    total_noodles_needed = beef * noodles_per_beef - noodles_already_have
    noodles_per_package = 2
    packages_needed = total_noodles_needed / noodles_per_package
    result = packages_needed
    return result

print(solution())