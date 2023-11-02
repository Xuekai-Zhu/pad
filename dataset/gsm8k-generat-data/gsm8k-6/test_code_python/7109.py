def solution():
    # Let X be the number of cans Michelle had to start with
    # X was split among Roger and 3 of his friends, so they each got X/4 cans
    # Roger gave away 2 cans and now has 4 cans, so he originally had (X/4) + 2 cans
    # Thus, (X/4) + 2 = 4, which means (X/4) = 2 and X = 8
    initial_cans = 8
    result = initial_cans
    return result

print(solution())