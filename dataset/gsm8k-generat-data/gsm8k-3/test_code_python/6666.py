def solution():
    """David is taking a data analytics course that lasts for 24 weeks.
    The course consists of 2 three-hour classes and 1 four-hour class each week.
    In addition, David must spend 4 hours each week working on small group homework assignments.
    How many hours will he spend on this course?"""
    
    # Define the number of classes each week and their duration
    num_classes_per_week = 3
    duration_1 = 3
    duration_2 = 3
    duration_3 = 4
    
    # Define the number of hours spent on small group homework assignments each week
    hours_spent_on_homework_per_week = 4
    
    # Calculate the total number of hours spent in class
    total_class_hours = num_classes_per_week * (duration_1 + duration_2 + duration_3) * 24
    
    # Calculate the total number of hours spent on small group homework assignments
    total_homework_hours = hours_spent_on_homework_per_week * 24
    
    # Calculate the total number of hours spent on the course
    total_hours = total_class_hours + total_homework_hours
    
    # Display the total number of hours spent on the course
    result = total_hours
    return result

print(solution())