def solution():
    num_courses = 4
    weekly_hours = 48
    num_weeks = 4
    hourly_rate = 25

    # Calculate the total number of hours Cindy worked in a month
    total_hours = weekly_hours * num_weeks

    # Calculate the total number of hours Cindy worked per course
    hours_per_course = total_hours / num_courses

    # Calculate the total pay for one course
    pay_per_course = hours_per_course * hourly_rate

    result = pay_per_course
    return result

print(solution())