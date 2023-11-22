def solution():
    
    # Define the total number of fourth-graders
    total_students = 96

    # Calculate the number of girls
    girls = 43

    # Calculate the number of absent girls
    absent_girls = 5

    # Calculate the number of absent boys
    absent_boys = 4

    # Calculate the number of fourth-grade boys
    fourth_graders = total_students - girls - absent_girls

    # Display the number of fourth grade boys
    result = fourth_graders
    return result

print(solution())