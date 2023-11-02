def solution():
    art_deco_start_year = 1920
    andy_birth_year = 1928
    andy_drawing_start_grade = 3
    
    if andy_birth_year > art_deco_start_year and andy_drawing_start_grade <= 1920:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())