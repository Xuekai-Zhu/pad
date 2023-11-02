def solution():
    num_classes_per_week = 3  # David has 2 three-hour classes and 1 four-hour class each week
    num_homework_hours_per_week = 4  # David must spend 4 hours each week working on small group homework assignments
    num_weeks = 24  # The course lasts for 24 weeks

    # Calculate the total number of hours David will spend in class
    total_class_hours = num_classes_per_week * (3 + 3 + 4) * num_weeks  # 2 three-hour classes and 1 four-hour class each week

    # Calculate the total number of hours David will spend on homework assignments
    total_homework_hours = num_homework_hours_per_week * num_weeks

    # Calculate the total number of hours David will spend on the course
    total_hours = total_class_hours + total_homework_hours
    result = total_hours
    return result

print(solution())