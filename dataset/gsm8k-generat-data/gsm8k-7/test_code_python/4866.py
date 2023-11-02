def solution():
    num_male_students = 29
    num_female_students = 4 * num_male_students
    total_students = num_male_students + num_female_students
    num_benches = 29

    # Calculate the minimum number of students that can sit on each bench
    # by dividing the total number of students by the number of benches
    min_students_per_bench = total_students / num_benches
    result = min_students_per_bench
    return result

print(solution())