def solution():
    """Justin and Sabrina at Pine Grove Elementary have 50 pencils combined.
    Justin has 8 more than twice as many pencils as Sabrina. How many pencils does Sabrina have?"""
    total_pencils = 50
    j_pencils = 2*s_pencils + 8
    j_and_s_pencils = j_pencils + s_pencils
    s_pencils = (total_pencils - j_and_s_pencils)/(-1)
    result = s_pencils
    return result

print(solution())