def solution():
    """Tom decides to make lasagna with all his beef. It takes twice as many noodles as beef. He has 10 pounds of beef. He already has 4 pounds of lasagna noodles and the noodles come in 2-pound packages. How many packages does he need to buy?"""
    beef_weight = 10
    noodle_weight_ratio = 2
    noodle_weight = beef_weight * noodle_weight_ratio
    already_have_noodles = 4
    remaining_noodles_needed = noodle_weight - already_have_noodles
    packages_needed = (remaining_noodles_needed + 1) // 2 
    result = packages_needed
    return result

print(solution())