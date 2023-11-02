def solution():
    # Calculate the total number of students before adding a boy
    total_students_before = 11 + 13

    # Calculate the percentage of girls before adding a boy
    percentage_girls_before = (13 / total_students_before) * 100

    # Calculate the total number of students after adding a boy
    total_students_after = total_students_before + 1

    # Calculate the percentage of girls after adding a boy
    percentage_girls_after = (13 / total_students_after) * 100

    # Calculate the difference in the percentage of girls before and after adding a boy
    percentage_difference = percentage_girls_after - percentage_girls_before

    result = percentage_girls_after
    return result

print(solution())