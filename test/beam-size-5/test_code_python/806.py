def solution():
    
    # Define the initial number of students on campus
    initial_students = 10

    # Calculate the number of students on campus after one month
    after_one_month = initial_students * 2

    # Calculate the number of students on campus after May
    after_may = after_one_month - (after_one_month * 12)

    # Calculate the additional students who would have joined by the end of May
    additional_students = after_may - initial_students

    # Display the additional students
    result = additional_students
    return result

print(solution())