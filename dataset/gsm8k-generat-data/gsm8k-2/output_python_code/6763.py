def solution():
    """A teacher is making packed lunches for a field trip. Each student needs 2 sandwiches, and will travel in a group with 5 other students. There are a total of 5 groups. How many pieces of bread will the teacher need to make enough sandwiches for all the students?"""
    sandwiches_per_student = 2
    students_per_group = 6
    total_groups = 5
    total_students = students_per_group * total_groups
    total_sandwiches = sandwiches_per_student * total_students
    total_bread_slices = total_sandwiches * 2
    result = total_bread_slices
    return result

print(solution())