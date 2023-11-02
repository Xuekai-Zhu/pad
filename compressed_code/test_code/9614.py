def solution():
    
    male_students = 29
    female_students = male_students * 4
    total_students = male_students + female_students
    benches = 29
    min_students_per_bench = (total_students + benches - 1) // benches
    result = min_students_per_bench
    return result

print(solution())