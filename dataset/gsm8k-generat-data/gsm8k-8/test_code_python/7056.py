def solution():
    # Calculate the number of students in the biology hall
    biology_hall = 2 * 30

    # Calculate the total number of students in the general study hall and biology hall
    gen_bio_total = 30 + biology_hall

    # Calculate the number of students in the math hall
    math_hall = int((3/5) * gen_bio_total)

    # Calculate the total number of students in all halls
    total_students = 30 + biology_hall + math_hall
    result = total_students
    return result

print(solution())