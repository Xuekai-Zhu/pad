def solution():
    common_origins = ["Greek mythology"]
    narcissism_origin = "Greek mythology"
    if narcissism_origin not in common_origins:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())