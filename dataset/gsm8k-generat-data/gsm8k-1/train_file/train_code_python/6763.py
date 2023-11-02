def solution():
    """A teacher is making packed lunches for a field trip. Each student needs 2 sandwiches, and will travel in a group with 5 other students. There are a total of 5 groups. How many pieces of bread will the teacher need to make enough sandwiches for all the students?"""
    students_per_group = 6 
    sandwiches_per_student = 2
    total_students = students_per_group * 5
    total_sandwiches = total_students * sandwiches_per_student
    bread_slices_per_sandwich = 2
    bread_slices_needed = total_sandwiches * bread_slices_per_sandwich
    result = bread_slices_needed
    return result

print(solution())