def solution():
    
    jeff_pencils = 300
    jeff_donated = 0.3 * jeff_pencils
    jeff_remaining = jeff_pencils - jeff_donated
    vicki_pencils = 2 * jeff_pencils
    vicki_donated = 0.75 * vicki_pencils
    vicki_remaining = vicki_pencils - vicki_donated
    total_remaining = jeff_remaining + vicki_remaining
    result = total_remaining
    return result

print(solution())