def solution():
    julia_projects = 64
    eric_projects = 577
    emma_projects = 0 # unknown
    if julia_projects < eric_projects:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())