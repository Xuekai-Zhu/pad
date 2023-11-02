def solution():
    # Calculate the number of students in the lunchroom
    total_monitors = 8  # given
    monitors_per_students = 2/15  # given
    total_students = round(total_monitors / monitors_per_students)

    # Calculate the number of boys and girls in the lunchroom
    girls_percentage = 40  # given
    boys_percentage = 100 - girls_percentage
    boys = round(total_students * boys_percentage / 100)
    girls = total_students - boys

    # Calculate the total number of cartons of milk consumed by the students
    total_milk = boys * 1 + girls * 2  # given
    result = total_milk
    return result

print(solution())