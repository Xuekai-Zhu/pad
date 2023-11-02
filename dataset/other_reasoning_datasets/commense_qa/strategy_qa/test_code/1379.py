def solution():
    condition = "Multiple Sclerosis"
    is_progressive = True
    waiver_policy = "no waivers for serious progressive conditions"
    if is_progressive and condition in waiver_policy:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())