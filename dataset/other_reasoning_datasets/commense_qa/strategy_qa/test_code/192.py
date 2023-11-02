def solution():
    common_era_duration = 2000
    tree_lifespan = 5000
    if common_era_duration < tree_lifespan:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())