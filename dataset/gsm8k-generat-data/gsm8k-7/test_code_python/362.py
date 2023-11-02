def solution():
    karen_weight = 8

    # First, we can use the statement "Karen's work tote bag is twice the weight of her husband Kevin's briefcase
    # when the briefcase is empty" to set up an equation:
    # 2x = y, where x is the weight of the empty briefcase and y is the weight of Karen's tote.
    # We know that y = 8, so we can solve for x:
    x = karen_weight / 2

    # Next, we know that "when Kevin puts his laptop and work papers in his briefcase, it is twice the weight
    # of Karen's tote." Let z be the weight of Kevin's laptop and work papers. Then we have:
    # x + z = 2y
    # We also know that "Kevin's work papers are a sixth of the weight of the contents of his full briefcase",
    # so we can set up another equation:
    # z = (1/6)(x + z) + w, where w is the weight of Kevin's laptop.
    # We can solve this equation for z:
    z = (1/5)x - w

    # We want to find out how many more pounds Kevin's laptop weighs than Karen's tote, so we can compute:
    difference = abs(w - karen_weight)
    result = difference
    return result

print(solution())