def solution():
    """There are 13 3-year-olds, 20 4-year-olds, 15 5-year-olds, and 22 six-year-olds at a particular Sunday school. If the 3 and 4-year-olds are in one class and the 5 and 6-year-olds are in another class, what is the average class size?"""
    # Define the number of students in each age group
    age_3 = 13
    age_4 = 20
    age_5 = 15
    age_6 = 22

    # Calculate the total number of students in each class
    class_1 = age_3 + age_4
    class_2 = age_5 + age_6

    # Calculate the average class size
    average_class_size = (class_1 + class_2) / 2

    # Display the average class size
    result = average_class_size
    return result

print(solution())