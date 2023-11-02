def solution():
    """Every week, Lucas makes 4 pieces of chocolate candy for each of his students on Monday. He made 40 pieces of chocolate candy last Monday. This upcoming Monday, 3 of Lucas' students will not be coming to class. How many pieces of chocolate candy will Lucas make for his class on Monday?"""
    # Define the initial number of students and pieces of candy made
    initial_students = 0
    initial_candy = 40

    # Calculate the number of students last Monday
    initial_students = initial_candy / 4

    # Calculate the number of students this Monday
    remaining_students = initial_students - 3

    # Calculate the number of pieces of candy to make this Monday
    candy_this_week = remaining_students * 4

    result = candy_this_week
    return result

print(solution())