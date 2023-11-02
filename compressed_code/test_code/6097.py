def solution():
    
    total_pencils = 50
    manny_pencils = 10
    nilo_pencils = manny_pencils + 10
    pencils_given = manny_pencils + nilo_pencils
    pencils_kept = total_pencils - pencils_given
    result = pencils_kept
    return result

print(solution())