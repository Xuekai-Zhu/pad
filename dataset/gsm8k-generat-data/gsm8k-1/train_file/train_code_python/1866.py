def solution():
    """There are 20 students in a class. Only one-fourth of the students stayed in the classroom while the rest went to the playground. Of those who went to the playground, one-third are boys. How many girls are there on the playground from this class?"""
    total_students = 20
    in_classroom = total_students // 4
    on_playground = total_students - in_classroom
    boys_on_playground = on_playground // 3
    girls_on_playground = on_playground - boys_on_playground
    result = girls_on_playground
    return result

print(solution())