def solution():
    num_general_hall = 30
    num_bio_hall = num_general_hall * 2
    num_math_hall = (num_general_hall + num_bio_hall) * 0.6

    total_students = num_general_hall + num_bio_hall + num_math_hall
    result = total_students
    return result

print(solution())