def solution():
    num_weeks = 24
    num_3hour_classes_per_week = 2
    num_4hour_classes_per_week = 1
    num_hours_spent_on_homework_per_week = 4

    # Calculate the total number of hours of 3-hour classes
    total_3hour_class_time = num_3hour_classes_per_week * 3 * num_weeks

    # Calculate the total number of hours of 4-hour classes
    total_4hour_class_time = num_4hour_classes_per_week * 4 * num_weeks

    # Calculate the total number of hours spent on homework
    total_homework_time = num_hours_spent_on_homework_per_week * num_weeks

    # Calculate the total number of hours spent on the course
    total_course_time = total_3hour_class_time + total_4hour_class_time + total_homework_time
    result = total_course_time
    return result

print(solution())