def solution():
    # Calculate the number of students who entered the bus at the intermediate stop
    initial_students_on_bus = 28
    final_students_on_bus = 58
    students_entered_at_stop = final_students_on_bus - initial_students_on_bus

    # Calculate 40% of the students who entered at the stop
    percent = 0.4
    percent_of_students = percent * students_entered_at_stop

    result = percent_of_students
    return result

print(solution())