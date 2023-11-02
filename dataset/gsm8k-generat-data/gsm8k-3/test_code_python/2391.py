def solution():
    """Every week, Lucas makes 4 pieces of chocolate candy for each of his students on Monday. He made 40 pieces of chocolate candy last Monday. This upcoming Monday, 3 of Lucas' students will not be coming to class. How many pieces of chocolate candy will Lucas make for his class on Monday?"""
    # Define the number of students Lucas has and the number of students absent
    num_students = 0
    num_absent = 3

    # Calculate the number of pieces of chocolate candy Lucas will make
    num_candy = (num_students - num_absent) * 4

    # Display the number of pieces of chocolate candy
    result = num_candy
    return result

print(solution())