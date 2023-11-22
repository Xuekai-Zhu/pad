def solution():
    
    # Define the total number of teachers
    total_teachers = 82

    # Calculate the number of teachers sick
    sick_teachers = 13

    # Calculate the number of teachers that were substitute in
    substitute_teachers = 9

    # Calculate the number of teachers that were at school that day
    school_teachers = total_teachers - sick_teachers - substitute_teachers

    # Display the number of teachers at school that day
    result = school_teachers
    return result

print(solution())