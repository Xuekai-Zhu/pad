def solution():
    num_boys = 11
    num_girls = 13
    total_students = num_boys + num_girls

    # Calculate the percentage of girls before adding a boy
    percentage_girls_before = (num_girls / total_students) * 100

    # Calculate the new total number of students after adding a boy
    new_total_students = total_students + 1

    # Calculate the new percentage of girls
    new_num_girls = num_girls
    new_percentage_girls = (new_num_girls / new_total_students) * 100

    # Calculate the percentage difference in the percentage of girls
    percentage_difference = abs(new_percentage_girls - percentage_girls_before)

    result = new_percentage_girls
    return result

print(solution())