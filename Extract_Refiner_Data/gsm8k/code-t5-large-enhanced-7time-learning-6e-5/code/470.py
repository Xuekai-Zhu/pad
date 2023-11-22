def solution():
    
    # Define the number of students who do not have desktop computers
    no_computers = 20

    # Calculate the number of students who have a desktop computer at home
    home_computers = no_computers * 0.75

    # Calculate the number of students at the grade level
    grade_level = home_computers + no_computers

    # Display the number of students at the grade level
    result = grade_level
    return result

print(solution())