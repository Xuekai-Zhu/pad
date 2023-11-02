def solution():
    """There are 13 3-year-olds, 20 4-year-olds, 15 5-year-olds, and 22 six-year-olds at a particular Sunday school. If the 3 and 4-year-olds are in one class and the 5 and 6-year-olds are in another class, what is the average class size?"""
    # Define the number of students in each age group
    age_3 = 13
    age_4 = 20
    age_5 = 15
    age_6 = 22

    # Calculate the total number of students in the combined 3 and 4-year-old class
    class_34 = age_3 + age_4

    # Calculate the total number of students in the combined 5 and 6-year-old class
    class_56 = age_5 + age_6

    # Calculate the average class size for each class
    avg_34 = class_34 / 2
    avg_56 = class_56 / 2

    # Calculate the overall average class size
    overall_avg = (class_34 + class_56) / 4

    # Return the result
    result = overall_avg
    return result

print(solution())