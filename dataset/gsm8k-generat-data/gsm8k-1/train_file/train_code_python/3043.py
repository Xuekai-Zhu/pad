def solution():
    """Tom decides to make lasagna with all his beef. It takes twice as many noodles as beef. He has 10 pounds of beef. He already has 4 pounds of lasagna noodles and the noodles come in 2-pound packages. How many packages does he need to buy?"""
    beef = 10
    noodles_per_beef = 2
    noodles_already_have = 4
    total_noodles_needed = beef * noodles_per_beef - noodles_already_have
    noodles_per_package = 2
    packages_needed = total_noodles_needed / noodles_per_package
    result = packages_needed
    return result

print(solution())