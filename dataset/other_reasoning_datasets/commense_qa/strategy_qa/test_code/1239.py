def solution():
    reject_food_stamps = True
    reject_medicaid_expansion = True
    reject_public_roads = False
    if reject_food_stamps and reject_medicaid_expansion and reject_public_roads:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())