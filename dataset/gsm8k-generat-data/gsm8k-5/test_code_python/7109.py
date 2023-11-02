def solution():
    # Let x be the number of cans Michelle had to start with
    # Michelle split x cans among 4 people, so each person got x/4 cans
    # Roger got x/4 cans and then gave away 2, so he ended up with (x/4)-2 cans
    # Roger now has 4 cans, so (x/4)-2 = 4
    # Solving for x, we get x = 24

    starting_cans = 24
    result = starting_cans
    return result

print(solution())