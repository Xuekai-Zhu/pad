def solution():
    """Every week, Lucas makes 4 pieces of chocolate candy for each of his students on Monday. He made 40 pieces of chocolate candy last Monday. This upcoming Monday, 3 of Lucas' students will not be coming to class. How many pieces of chocolate candy will Lucas make for his class on Monday?"""
    students = 4 * (40 / 4)  # There were 40 pieces of chocolate candy made for the entire original class
    remaining_students = students - (3 * 4)  # 3 students will not be coming to class
    pieces_of_candy = remaining_students * 4
    result = pieces_of_candy
    return result

print(solution())