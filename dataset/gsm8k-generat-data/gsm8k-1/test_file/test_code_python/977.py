def solution():
    """On Thursday, Joe caught 3 pounds of crawfish. He caught 4 times that amount on Friday and half the amount of his Friday's catch on Saturday. If 1 serving of crawfish is 3 pounds, how many servings does he have?"""
    thursday_catch = 3
    friday_catch = 4 * thursday_catch
    saturday_catch = friday_catch / 2
    total_catch = thursday_catch + friday_catch + saturday_catch
    servings = total_catch / 3
    result = servings
    return result

print(solution())