def solution():
    # Number of students in the general study hall
    gen_study = 30

    # Number of students in the biology hall
    bio = 2 * gen_study

    # Total number of students in the general study and biology halls combined
    gen_bio_total = gen_study + bio

    # Number of students in the math hall
    math = 3/5 * gen_bio_total

    # Total number of students
    total_students = gen_study + bio + math
    result = total_students
    return result

print(solution())