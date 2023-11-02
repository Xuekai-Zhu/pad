def solution():
    black_swan_status = "least concern"
    koala_status = "vulnerable"
    if koala_status > black_swan_status:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())