def solution():
    minimum_age = 18
    child_age = 17
    if child_age < minimum_age:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())