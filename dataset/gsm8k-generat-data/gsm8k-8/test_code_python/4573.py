def solution():
    # Define the ratio of boys to girls
    boys_to_girls_ratio = 3/5

    # Calculate the total number of students
    total_students = 4 / (1/boys_to_girls_ratio - 1)

    # Calculate the number of boys and girls
    boys = total_students / (1 + boys_to_girls_ratio)
    girls = total_students - boys

    # Calculate the final result
    result = total_students
    return result

print(solution())