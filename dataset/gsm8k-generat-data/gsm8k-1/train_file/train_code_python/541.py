def solution():
    """Every day, Sara bakes 10 cakes and puts them in his refrigerator. He does this for 5 days. Carol then comes over and eats 12 of his cakes. If it takes 2 cans of frosting to frost a single cake, how many cans of frosting does Bob need to frost the remaining cakes?"""
    total_cakes = 10 * 5
    eaten_cakes = 12
    remaining_cakes = total_cakes - eaten_cakes
    cans_of_frosting = remaining_cakes * 2
    result = cans_of_frosting
    return result

print(solution())