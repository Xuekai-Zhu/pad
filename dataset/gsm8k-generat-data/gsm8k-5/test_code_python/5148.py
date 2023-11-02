def solution():
    # Calculate the number of students in Monica's first, fourth, fifth, and sixth classes
    first_class = 20
    fourth_class = first_class / 2
    fifth_class = 28
    sixth_class = 28

    # Calculate the total number of students in Monica's second and third classes
    second_and_third_classes = 2 * 25

    # Calculate the total number of students Monica sees per day
    total_students = first_class + second_and_third_classes + fourth_class + fifth_class + sixth_class
    result = total_students
    return result

print(solution())