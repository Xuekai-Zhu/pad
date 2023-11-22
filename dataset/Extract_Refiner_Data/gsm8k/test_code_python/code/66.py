def solution():
    
    # Define the number of dance classes and the number of students per class
    dance_classes = 5
    students_per_class = 15

    # Calculate the total number of students Judy teaches in a week
    total_students = (dance_classes * students_per_class * 5) + (students_per_class * 8)

    # Calculate the total money Judy makes in a week
    total_money = total_students * 15

    # return the result
    result = total_money
    return result

print(solution())