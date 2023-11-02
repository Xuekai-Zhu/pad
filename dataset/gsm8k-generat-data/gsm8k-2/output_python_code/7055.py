def solution():
    """There are 30 students in the general study hall and twice as many students in the biology hall as there are in the general study hall. If the number of students in the math hall is 3/5 times as many as the combined total number of students in the general study hall and the biology hall combined, calculate the total number of students in all the halls combined."""
    gen_study_hall = 30
    bio_hall = 2 * gen_study_hall
    math_hall = 0.6 * (gen_study_hall + bio_hall)
    total_students = gen_study_hall + bio_hall + math_hall
    result = total_students
    return result

print(solution())