def solution():
    
    gen_study_hall = 30
    bio_hall = 2 * gen_study_hall
    math_hall = 0.6 * (gen_study_hall + bio_hall)
    total_students = gen_study_hall + bio_hall + math_hall
    result = total_students
    return result

print(solution())