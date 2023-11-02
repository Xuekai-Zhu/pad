def solution():
    """At Rainbow Preschool, there are 80 students. 25% of them are half-day students and get picked up at noon, while the rest are full-day students. How many are full-day students?"""
    total_students = 80
    half_day_students = total_students * 0.25
    full_day_students = total_students - half_day_students
    result = full_day_students
    return result

print(solution())