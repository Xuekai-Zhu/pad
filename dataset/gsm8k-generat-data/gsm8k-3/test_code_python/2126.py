def solution():
    """Adam teaches 50 students a year. How many students will Adam teach in 10 years if in the first year he only teaches 40 students?"""
    # Define the number of students Adam teaches in the first year
    first_year = 40

    # Define the number of students Adam teaches in each subsequent year
    annual_students = 50
    
    # Calculate the total number of students Adam will teach in 10 years
    total_students = first_year + (annual_students * 9)

    # Display the total number of students
    result = total_students
    return result

print(solution())