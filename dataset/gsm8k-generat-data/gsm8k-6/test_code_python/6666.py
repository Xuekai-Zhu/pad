def solution():
    # Calculate the total number of hours spent in class each week
    class_hours = (2 * 3) + 4  # 2 three-hour classes and 1 four-hour class
    total_weekly_hours = class_hours + 4  # class hours plus 4 hours for small group homework assignments

    # Calculate the total number of hours spent on the course
    total_hours = total_weekly_hours * 24  # 24 weeks in total
    result = total_hours
    return result

print(solution())