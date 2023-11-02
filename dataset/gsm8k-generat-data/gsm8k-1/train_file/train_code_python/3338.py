def solution():
    """In my school, the number of students has increased by 20% this year. The number of students this year is 960. How many students were there last year?"""
    current_students = 960
    percent_increase = 20
    previous_students = current_students / (1 + (percent_increase / 100))
    result = previous_students
    return result

print(solution())