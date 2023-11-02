def solution():
    wilson_party = "Democratic"
    taft_party = "Republican"
    harding_party = "Republican"
    if wilson_party != taft_party and wilson_party != harding_party and taft_party != harding_party:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())