def solution():
    """There are 20 students in a class. Only one-fourth of the students stayed in the classroom while the rest went to the playground. Of those who went to the playground, one-third are boys. How many girls are there on the playground from this class?"""
    total_students = 20
    classroom_students = total_students // 4
    playground_students = total_students - classroom_students
    boys_playground_students = playground_students // 3
    girls_playground_students = playground_students - boys_playground_students
    result = girls_playground_students
    return result

print(solution())