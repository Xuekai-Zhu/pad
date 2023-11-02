def solution():
    """David is taking a data analytics course that lasts for 24 weeks. The course consists of 2 three-hour classes and 1 four-hour class each week. In addition, David must spend 4 hours each week working on small group homework assignments. How many hours will he spend on this course?"""
    weeks = 24
    num_classes_per_week = 3
    total_hours_per_class = 2 * num_classes_per_week + 4
    homework_hours_per_week = 4
    total_hours_per_week = total_hours_per_class + homework_hours_per_week
    total_hours = total_hours_per_week * weeks
    result = total_hours
    return result

print(solution())