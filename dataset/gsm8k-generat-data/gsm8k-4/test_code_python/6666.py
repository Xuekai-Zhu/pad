def solution():
    """David is taking a data analytics course that lasts for 24 weeks. The course consists of 2 three-hour classes and 1 four-hour class each week. In addition, David must spend 4 hours each week working on small group homework assignments. How many hours will he spend on this course?"""
    # Define the number of weeks and class hours
    weeks = 24
    class_1_hours = 3
    class_2_hours = 3
    class_3_hours = 4
    
    # Define the number of hours spent on homework per week
    homework_hours = 4
    
    # Calculate the total number of class hours and homework hours
    class_total_hours = (class_1_hours + class_2_hours + class_3_hours) * weeks
    homework_total_hours = homework_hours * weeks
    
    # Calculate the total hours spent on the course
    total_hours = class_total_hours + homework_total_hours
    
    # return the result
    result = total_hours
    return result

print(solution())