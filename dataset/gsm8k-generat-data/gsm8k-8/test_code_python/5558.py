def solution():
    # Define the ratio of boys to girls
    boys_to_girls_ratio = 5/8

    # Calculate the total number of students in the class
    total_students = 260

    # Calculate the number of boys in the class
    boys = total_students / (1 + boys_to_girls_ratio)

    # Calculate the number of girls in the class
    girls = boys * boys_to_girls_ratio
    result = girls
    return result

print(solution())