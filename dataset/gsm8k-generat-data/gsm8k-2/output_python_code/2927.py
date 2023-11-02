def solution():
    """Oxford High School has 48 teachers, 1 principal and 15 classes with each having 20 students. How many people are there in total in Oxford High School?"""
    total_teachers = 48
    total_principal = 1
    total_students = 15 * 20
    total_people = total_teachers + total_principal + total_students
    result = total_people
    return result

print(solution())