def solution():
    
    # Define the number of students enrolled at Norman High School and Butler High School
    norman_students = 4000
    butler_students = (3/4) * norman_students

    # Calculate the average number of students enrolled at Norman High School and Butler High School
    avg_students = norman_students + butler_students

    # Calculate the difference in the number of students enrolled at Norman High School and Butler High School
    difference = avg_students - norman_students

    # Display the difference in the number of students enrolled at Norman High School
    result = difference
    return result

print(solution())