def solution():
    """In my school, the number of students has increased by 20% this year. The number of students this year is 960. How many students were there last year?"""
    current_num_students = 960
    percent_increase = 20
    # First we need to calculate what the original number of students was before the increase
    original_num_students = current_num_students / (1 + percent_increase/100)
    # Round the number to nearest integer
    original_num_students = round(original_num_students)
    result = original_num_students
    return result

print(solution())