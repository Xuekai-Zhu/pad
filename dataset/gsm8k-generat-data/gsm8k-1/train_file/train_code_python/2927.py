def solution():
    """Oxford High School has 48 teachers, 1 principal and 15 classes with each having 20 students. How many people are there in total in Oxford High School?"""
    num_teachers = 48
    num_principal = 1
    num_classes = 15
    num_students_per_class = 20
    
    total_students = num_classes * num_students_per_class
    total_people = num_teachers + num_principal + total_students
    result = total_people
    
    return result

print(solution())