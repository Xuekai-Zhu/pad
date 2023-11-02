def solution():
    number_of_kindergarteners = 26
    number_of_first_graders = 19
    number_of_second_graders = 20
    number_of_third_graders = 25
    total_number_of_students = number_of_kindergarteners + number_of_first_graders + number_of_second_graders + number_of_third_graders
    lice_checks_per_student = 2
    total_lice_checks = total_number_of_students * lice_checks_per_student
    minutes_per_hour = 60
    hours = total_lice_checks / minutes_per_hour
    result = hours
    
    return result

print(solution())