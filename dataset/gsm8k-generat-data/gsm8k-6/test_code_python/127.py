def solution():
    # Calculate the total number of meows made by all three cats in 5 minutes
    meows_cat1 = 3 * 5  # the first cat meows 3 times per minute for 5 minutes
    meows_cat2 = 2 * meows_cat1  # the second cat meows twice as frequently as the first cat
    meows_cat3 = 1/3 * meows_cat2  # the third cat meows at one-third the frequency of the second cat
    total_meows = meows_cat1 + meows_cat2 + meows_cat3
    result = total_meows
    return result

print(solution())