def solution():
    # Number of bags picked by Dallas
    apples_dallas = 14
    pears_dallas = 9

    # Number of bags picked by Austin
    apples_austin = apples_dallas + 6
    pears_austin = pears_dallas - 5

    # Total number of bags picked by Austin
    total_bags_austin = apples_austin + pears_austin
    result = total_bags_austin
    return result

print(solution())