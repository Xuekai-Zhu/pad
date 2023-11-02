def solution():
    total_students = 240
    num_three_or_more = (1/6) * total_students
    num_two = 0.35 * total_students
    num_one = (5/12) * total_students

    # Calculate the number of students who do not read novels
    num_none = total_students - num_three_or_more - num_two - num_one
    result = num_none
    return result

print(solution())