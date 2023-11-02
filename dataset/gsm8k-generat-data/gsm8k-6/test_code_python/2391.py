def solution():
    # Calculate the total number of students in Lucas' class
    total_students = 40 // 4  # Lucas made 40 pieces of chocolate candy last Monday, and he made 4 pieces for each student

    # Calculate the number of students who will be present on the upcoming Monday
    present_students = total_students - 3  # 3 students will not be coming to class

    # Calculate the total number of pieces of chocolate candy Lucas will make
    total_candy = present_students * 4  # Lucas makes 4 pieces of chocolate candy for each present student
    result = total_candy
    return result

print(solution())