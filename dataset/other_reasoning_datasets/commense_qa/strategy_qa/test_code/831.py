def solution():
    target_age_group = "children"
    extra_wheels = 2
    if target_age_group == "children" and extra_wheels > 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())