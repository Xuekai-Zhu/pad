def solution():
    """In my school, the number of students has increased by 20% this year. The number of students this year is 960. How many students were there last year?"""
    # Define the percentage increase and the number of students this year
    INCREASE_PERCENTAGE = 20
    students_current = 960

    # Calculate the number of students last year
    students_last_year = students_current / (1 + INCREASE_PERCENTAGE / 100) 

    result = students_last_year
    return result

print(solution())