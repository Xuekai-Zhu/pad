def solution():
    """Every day, Sara bakes 10 cakes and puts them in his refrigerator. He does this for 5 days. Carol then comes over and eats 12 of his cakes. If it takes 2 cans of frosting to frost a single cake, how many cans of frosting does Bob need to frost the remaining cakes?"""
    # Calculate the total number of cakes baked by Sara
    total_cakes = 10 * 5

    # Calculate the number of cakes remaining after Carol eats 12
    remaining_cakes = total_cakes - 12

    # Calculate the number of cans of frosting needed to frost the remaining cakes
    frosting_cans = remaining_cakes * 2

    # return the result
    result = frosting_cans
    return result

print(solution())