def solution():
    """In my school, the number of students has increased by 20% this year. The number of students this year is 960. How many students were there last year?"""
    # Define the increase percentage and the number of students this year
    increase_percentage = 20
    students_this_year = 960

    # Calculate the number of students last year using the increase percentage
    students_last_year = students_this_year / (1 + (increase_percentage / 100))

    # Round the result to the nearest whole number and return it
    result = round(students_last_year)
    return result

print(solution())