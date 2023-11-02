def solution():
    """If there were 200 students who passed an English course three years ago, and each subsequent year until the current one that number increased by 50% of the previous year's number, how many students will pass the course this year?"""
    # Define the number of students who passed three years ago
    students_3_years_ago = 200

    # Calculate the number of students who passed in the subsequent years
    students_last_year = students_3_years_ago * 1.5
    students_2_years_ago = students_3_years_ago + students_last_year
    students_this_year = students_last_year * 1.5 + students_2_years_ago

    # Display the total number of students who passed this year
    result = students_this_year
    return result

print(solution())