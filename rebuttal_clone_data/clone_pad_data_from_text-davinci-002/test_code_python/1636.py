def solution():
    hours_in_school = 7.5
    total_classes = 7
    combined_history_and_chemistry_class_time = 1.5
    other_classes = total_classes - combined_history_and_chemistry_class_time
    average_class_time = other_classes / hours_in_school
    result = average_class_time
    return result

print(solution())