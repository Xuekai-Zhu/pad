def solution():
    
    total_pencils = 50
    manny_pencils = 10
    nilo_pencils = manny_pencils + 10
    given_pencils = manny_pencils + nilo_pencils
    kept_pencils = total_pencils - given_pencils
    result = kept_pencils
    return result

print(solution())