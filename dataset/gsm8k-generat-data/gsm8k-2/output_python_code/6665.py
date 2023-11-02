def solution():
    """David is taking a data analytics course that lasts for 24 weeks. The course consists of 2 three-hour classes and 1 four-hour class each week. In addition, David must spend 4 hours each week working on small group homework assignments. How many hours will he spend on this course?"""
    class_hours = (2 * 3) + 4
    weekly_hours = class_hours + 4
    total_hours = weekly_hours * 24
    result = total_hours
    return result

print(solution())