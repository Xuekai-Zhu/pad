def solution():
    # Define the total number of students
    total_students = 100

    # Calculate the number of men as a proportion of total students
    men_proportion = 0.7

    # Calculate the number of men as a difference between total students and women
    men = (total_students - 180) * men_proportion
    result = men
    return result

print(solution())