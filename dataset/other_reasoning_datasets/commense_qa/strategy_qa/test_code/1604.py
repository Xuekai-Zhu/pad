def solution():
    christian_percent = 83
    atheist_percent = 100 - christian_percent
    if atheist_percent < christian_percent:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())