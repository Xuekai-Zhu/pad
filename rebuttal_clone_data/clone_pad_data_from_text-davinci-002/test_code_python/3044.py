def solution():
    beef = 10
    noodles_per_beef = 2
    owned_noodles = 4
    package_size = 2
    needed_noodles = beef * noodles_per_beef - owned_noodles
    needed_packages = needed_noodles / package_size
    result = needed_packages
    
    return result

print(solution())