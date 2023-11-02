def solution():
    male_students = 29
    female_students = 4 * male_students
    total_students = male_students + female_students
    benches = 29
    students_per_bench = total_students / benches
    result = students_per_bench
    return result

print(solution())