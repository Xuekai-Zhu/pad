def solution():
    jeff_pencils = 300
    vicki_pencils = jeff_pencils * 2
    jeff_donated = jeff_pencils * 0.3
    vicki_donated = vicki_pencils * 0.75
    remaining = jeff_pencils - jeff_donated + vicki_pencils - vicki_donated
    result = remaining
    return result

print(solution())