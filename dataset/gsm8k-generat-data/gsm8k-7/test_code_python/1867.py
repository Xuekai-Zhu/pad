def solution():
    num_students = 20

    # Calculate the number of students who stayed in the classroom
    num_stayed = num_students / 4

    # Calculate the number of students who went to the playground
    num_playground = num_students - num_stayed

    # Calculate the number of boys on the playground
    num_boys = num_playground / 3

    # Calculate the number of girls on the playground
    num_girls = num_playground - num_boys
    
    result = num_girls
    return result

print(solution())