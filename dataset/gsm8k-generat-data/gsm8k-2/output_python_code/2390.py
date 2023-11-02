def solution():
    """Every week, Lucas makes 4 pieces of chocolate candy for each of his students on Monday. He made 40 pieces of chocolate candy last Monday. This upcoming Monday, 3 of Lucas' students will not be coming to class. How many pieces of chocolate candy will Lucas make for his class on Monday?"""
    candy_per_student = 4
    total_students = 20 # assuming that there are 20 students in Lucas' class
    initial_candy = 40
    remaining_students = total_students - 3
    total_candy = (remaining_students * candy_per_student) + initial_candy
    result = total_candy
    return result

print(solution())