def solution():
    left_college = True
    latin_honors_require_degree = True
    if left_college or not latin_honors_require_degree:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())